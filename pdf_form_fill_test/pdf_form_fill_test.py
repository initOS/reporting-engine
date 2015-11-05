# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2010-2014 OpenERP s.a. (<http://openerp.com>).
#    Copyright (C) 2015 initOS GmbH(<http://www.initos.com>).
#    Author Nikolina Todorova <nikolina.todorova@initos.com>
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

from openerp.osv import fields, orm
import os


class pdf_form_fill_test(orm.Model):
    _name = "pdf.form.fill.test"
    _inherit = 'pdf.form.fill'

    def get_directory_name(self):
        return os.path.dirname(__file__)

    def download_pdf_form(self, cr, uid, ids, field_name=None,
                          arg=None, context=None):
        result = {}
        for id in ids:
            result.update(super(pdf_form_fill_test,
                                self).download_pdf_form(cr, uid, [id],
                                                        field_name, arg,
                                                        context=context))
        return result

    _columns = {
        'first_name': fields.char('First Name'),
        'last_name': fields.char('Last Name'),
        'pdf_file': fields.function(download_pdf_form, method=True,
                                    store=False, type='binary',
                                    string="Download File"),
    }

    def prepare_pdf_fields(self, cr, uid, ids, context=None):
        """Overwrite this to add specific preparations.
           Return value has to be a list of tupel ('pdf field name', value)
        """
        obj = self.browse(cr, uid, ids, context=context)

        return [('first_name_text', obj[0].first_name),
                ('last_name_text', obj[0].last_name)]

    def get_pdf_file_path(self, cr, uid, ids, context=None):
        """Overwrite this to return the specific pdf file path."""
        return os.path.join(os.path.join(self.get_directory_name(),
                                         "data/pdf_form_fill_test_form.pdf"))
