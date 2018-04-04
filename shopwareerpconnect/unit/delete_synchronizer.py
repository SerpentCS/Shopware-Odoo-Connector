# -*- coding: utf-8 -*-
##############################################################################
#
#    Authors: Guewen Baconnier, Oliver Görtz
#    Copyright 2013 Camptocamp SA, Oliver Görtz
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from odoo.tools.translate import _
from odoo.addons.queue_job.job import job, related_action
from odoo.addons.connector.unit.synchronizer import Deleter
from ..models.connector import get_environment
from ..models.related_action import link


class ShopwareDeleter(Deleter):
    """ Base deleter for Shopware """

    def run(self, shopware_id):
        """ Run the synchronization, delete the record on Shopware

        :param shopware_id: identifier of the record to delete
        """
        self.backend_adapter.delete(shopware_id)
        return _('Record %s deleted on Shopware') % shopware_id


ShopwareDeleteSynchronizer = ShopwareDeleter  # deprecated


@job(default_channel='root.shopware')
@related_action(action=link)
def export_delete_record(session, model_name, backend_id, shopware_id):
    """ Delete a record on Shopware """
    env = get_environment(session, model_name, backend_id)
    deleter = env.get_connector_unit(ShopwareDeleter)
    return deleter.run(shopware_id)
