# -*- coding: utf-8 -*-
from openerp.osv import fields, osv

class confirmation(osv.osv_memory):
    
    _name = "sale_order_confirm_cancel.confirmation"
    
    def cancel_quotation(self, cr, uid, ids, context=None):

        if not context:
            context = {}
    
        return self.pool.get('sale.order').action_cancel(cr, uid, context.get('active_ids',[]), context)