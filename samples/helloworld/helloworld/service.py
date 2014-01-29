import gevent
from gevent import monkey
from datetime import datetime
from datetime import timedelta
import traceback
from novaclient.v1_1 import client as nclient
from oslo.config import cfg
from helloworld.openstack.common import log
from helloworld.openstack.common import service

monkey.patch_socket()
monkey.patch_ssl()

CONF = cfg.CONF
LOG = log.getLogger(__name__)

CONF.register_opts([cfg.IntOpt("sleep_interval_sec",
                               default=3600,
                               help="Time interval (secs) between two consecutive runs.")],
                   group="service")

CONF.register_opts([cfg.StrOpt('username',
                               help='OpenStack username',
                               required=True),
                    cfg.StrOpt('password',
                               help='OpenStack password',
                               required=True),
                    cfg.StrOpt('tenant_name',
                               help='OpenStack tenant name',
                               required=True),
                    cfg.StrOpt('tenant_id',
                               help='OpenStack tenant id',
                               required=True),
                    cfg.StrOpt('auth_url',
                               help='OpenStack auth URL',
                               required=True)],
                   group="helloworld")


class Service(service.Service):
    """Service object for binaries running on hosts."""

    def __init__(self):
        service.Service.__init__(self)
        self.nova_client = nclient.Client(CONF.helloworld.username,
                                          CONF.helloworld.password,
                                          CONF.helloworld.tenant_name,
                                          auth_url=CONF.helloworld.auth_url)

    def start(self):
        super(Service, self).start()
        self.crawler = gevent.Greenlet.spawn(self.run)
        gevent.Greenlet.join(self.crawler)

    def stop(self):
        try:
            self.crawler.kill()
        except Exception as e:
            LOG.error(e)
            traceback.print_exc()

    def run(self):
        while True:
            LOG.info("Starting a run......")
            start = datetime.now()

            flavors = self.nova_client.flavors.list()
            for flavor in flavors:
                LOG.debug("Flavor ID: {id}, Flavor Name: {name}".format(id=flavor.id, name=flavor.name))

            LOG.info("Last run took {elapsed_time}".format(
                elapsed_time=datetime.now() - start))
            next_run_time = datetime.now() + \
                            timedelta(seconds=CONF.service.sleep_interval_sec)
            LOG.info("Next run will be at " + str(next_run_time))
            gevent.sleep(CONF.service.sleep_interval_sec)
