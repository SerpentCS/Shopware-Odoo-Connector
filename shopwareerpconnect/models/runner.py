from openerp import models,fields
from ..unit.import_synchronizer import ShopwareImporter
from openerp.addons.connector.connector import ConnectorEnvironment

class QueueJobRunner(models.Model):

	_name="queue.job.runner"
	_description="Run all jobs that are in pending state"

	def run_jobs(self, cr, uid, max_count=None):
		runner = ShopwareImporter()
		runner.run()