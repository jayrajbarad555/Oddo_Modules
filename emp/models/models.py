# -*- coding: utf-8 -*-

from odoo import models, fields, api


#****************************** START FOR EMP MENU ****************************************************


class emp(models.Model):
    _name = 'emp.emp'
    _description = 'employees data'
    
#     employee_type = fields.Selection([
#     ('employee', 'Employee'),
#     ('manager', 'Manager'),
#     ('admin', 'Admin'),
# ], string='Employee Type', default='employee')


    name = fields.Char(string = 'Employees Name',required = True,size=1000)
    work_mobile = fields.Char(string='Work Mobile')
    work_phone= fields.Char(string='Work phone')
    work_email = fields.Char(string='Work Email')
    job_position = fields.Char(string='Job Position')
    manager_id = fields.Many2one('res.users', 'Manager', store=True, readonly=False)

    coach_id = fields.Many2one('emp.emp', string='Coach')
    
    # ------------------------__for work information__---------------------------------------------
    
    # -------------------------------LOCATION------------------------------------------------------ 
    work_location_id = fields.Many2one('emp.emp', string = 'work location')
    address_id = fields.Many2one('emp.emp',string = "work Address")
    #----------------------------------------------------------------------------------------------
    
    # -------------------------------SCHEDULE-----------------------------------------------------
    resource_calendar_id = fields.Many2one('emp.emp', string= ' working_hours')
    time_zone = fields.Many2one('emp.emp', string= ' Time Zone')
    #----------------------------------------------------------------------------------------------
    
    # ------------------------__private information__----------------------------------------------
    
    # ----------------------------PRIVATE CONTECT--------------------------------------------------
    address_home_id = fields.Char(string = 'Address')
    language= fields.Many2one('emp.emp',string = 'Language')
    home_distance = fields.Integer(string = ' Home Work Distance')
    #----------------------------------------------------------------------------------------------
   
    # --------------------------------EDUCATION----------------------------------------------------  
    certificate = fields.Selection([
        ('graduate', 'Graduate'),
        ('bachelor', 'Bachelor'),
        ('master', 'Master'),
        ('doctor', 'Doctor'),
        ('other', 'Other'),
    ])
    study_field = fields.Char("Field of Study")
    study_school = fields.Char("School")
   #----------------------------------------------------------------------------------------------- 
    
   # --------------------------------PRIVATE CONTECT------------------------------------------------
    permit_no = fields.Char('Work Permit No')
    visa_no = fields.Char('Visa No')
    visa_expire = fields.Date('Visa Expire Date')
    work_permit_expiration_date = fields.Date('Work Permit Expiration Date')
    # has_work_permit = fields.Binary(string="Work Permit")
    work_permit_name = fields.Char('work_permit_name')
   #-------------------------------------------------------------------------------------------------
   #-----------------------------------FAMILY STATUS-------------------------------------------------
    marital = fields.Selection([
        ('single', 'Single'),
        ('married', 'Married'),
        ('cohabitant', 'Legal Cohabitant'),
        ('widower', 'Widower'),
        ('divorced', 'Divorced')
    ], string='Marital Status')
    children = fields.Integer(string='Number of Dependent Children') 
    #-------------------------------------------------------------------------------------------------
    
    #-----------------------------EMERGENCY-----------------------------------------------------------
    emergency_contact = fields.Char("Contact Name", groups="hr.group_hr_user", tracking=True)
    emergency_phone = fields.Char("Contact Phone", groups="hr.group_hr_user", tracking=True)
    #-------------------------------------------------------------------------------------------------
    
    #------------------------------CITIZENSHIP--------------------------------------------------------
    country_id = fields.Many2one(
        'emp.emp', 'Nationality (Country)', groups="hr.group_hr_user", tracking=True)
    identification_id = fields.Char(string='Identification No')
    passport_id = fields.Char('Passport No')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ])
    birthday = fields.Date('Date of Birth')
    place_of_birth = fields.Char('Place of Birth')
    country_of_birth = fields.Many2one('emp.emp', string="Country of Birth")
   #--------------------------------------------------------------------------------------------------
   
   
   #------------------------------------__HR Setting__------------------------------------------------
   
   #----------------------------------------STATUS----------------------------------------------------
    user_id = fields.Many2one('emp.emp', 'User')
   #--------------------------------------------------------------------------------------------------
   
   #---------------------------------Attendance/Point of Sale-----------------------------------------
    pin = fields.Char(string="PIN")
   #--------------------------------------------------------------------------------------------------
   
# ********************************* END FOR EMP MENU ****************************************************
 
# ***************************** START FOR DEPARTMENT MENU ***********************************************
   
   
# field_name = fields.Char(
#     string='Field Name',
#     groups="module.group_employee, module.group_manager",
# )

class Department(models.Model):
    _name = "emp.department"
    _description = "Department"


    name = fields.Char('Dept Name', required=True)
    parent_id = fields.Many2one('emp.department', string='Parent Department')
    manager_id = fields.Many2one('emp.department', string='Manager')
    
# ***************************** END FOR DEPARTMENT MENU ***********************************************

# ***************************** START FOR configuration MENU ***********************************************

    
class empDepartment(models.Model):
    _name = "emp.dept"
    _description = "employee department"
    
    name = fields.Char('Dept Name', required=True)
    parent_id = fields.Many2one('emp.department', string='Parent Department')
    manager_id = fields.Many2one('emp.department', string='Manager')
    
    
class workLocation(models.Model):
    _name = "emp.work_location"
    _description = "employee work location"
    
    work_location = fields.Many2one('emp.emp', string = 'work location')
    address = fields.Many2one('emp.emp',string = "work Address")
    
class tags(models.Model):
    _name = "emp.tags"
    _description = "employee tags"
    
    name = fields.Char(string='Tag name')
    
    
class jobposition(models.Model):
    _name = "emp.jobposition"
    _description = "employee job position"
    
    job_position = fields.Char(string='Job Position')
    department_name = fields.Char(string = 'Department')
    employee_type_id = fields.Many2one('emp.jobposition', string='Employment Type')
    description = fields.Html(string='Job Description')
    
    
class employeeType(models.Model):
    _name = "emp.emptype"
    _description = "employee types"
    
    name = fields.Char(string = 'Name')
    
    
class on_offboarding(models.Model):
    _name = "emp.plan"
    _description = "On\Off boarding plans"
    
    name = fields.Char(string = 'Plan Name',required=True)
    department_name = fields.Char(string = 'Department')
    Name = fields.Char(string = 'Name',required = True)

  
class badges(models.Model):
    _name = "emp.badges"
    _description = "Badges"
    
    name = fields.Char(string = 'Badge') 
      
   
   
   
   
   
   
   
   
   
   
   
   
   
    # value = fields.Integer()
    # value2 = fields.Float(compute="_value_pc", store=True)
    # description = fields.Text()

    
    