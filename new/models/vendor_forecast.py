# -*- coding: utf-8 -*-


from odoo import models, fields, api

class VendorForecast(models.Model):
    _name = 'new.forecast'
    _description = 'Forecast details'

    #---------Fields to store forecast information-------#
    
    product_name = fields.Char(string = 'Product Name')
    expected_quantity = fields.Integer(string='Expected Quantity')
    forecast_date = fields.Date(string='Forecast Date')
    product_id = fields.Many2one('new.forecast', string='Product')


   



    
