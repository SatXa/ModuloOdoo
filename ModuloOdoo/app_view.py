<?xml version="1.0" encoding="UTF-8"?>
    <openerp>
        <data>
			<record id="view_form_aplicacion_ejemplo01_task" model="ir.ui.view">
                <field name="name">Aplicacion Task Form</field>
                <field name="model">aplicacion.task</field>
                <field name="arch" type="xml">
                <form>
                    <header>
                        <button name="do_toggle_done" type="object" string="Toggle Done" class="oe_highlight" />
                        <button name="do_clear_done" type="object" string="Clear All Done" />
                    </header>
                    <sheet>
                        <group name="group_top">
                            <group name="group_left">
                                <field name="name"/>
                            </group>
                            <group name="group_right">
                                <field name="is_done"/>
                                <field name="active" readonly="1" />
                            </group>
                        </group>
                    </sheet>
                </form>
                </field>
            </record>
			
			"""<record id="view_form_aplicacion_task" model="ir.ui.view">
				<field name="name">Aplicacion Task Form</field>
				<field name="model">aplicacion.task</field>
				<field name="arch" type="xml">
					<form string="Aplicacion Task">
						<field name="name"/>
						<field name="is_done"/>
						<field name="active" readonly="1"/>
					</form>
				</field>
			</record>"""
		
            <!-- Action to open To-do Task list -->
            <act_window
                id="action_unfold_menu"
                name="Name Action"
                res_model="aplicacion.task"
                view_mode="tree,form"
            />
            <!-- Menu item to open aplicacion Task list -->
            <menuitem
                id="menu"
                name="Name Menu"
#                parent="mail.mail_feeds"
                sequence="20"
                action="action_unfold_menu"
            />
        </data>
    </openerp>