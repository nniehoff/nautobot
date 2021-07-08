from nautobot.core.apps import NavMenuAddButton, NavMenuGroup, NavMenuItem, NavMenuImportButton, NavMenuTab


menu_items = (
    NavMenuTab(
        name="Organization",
        weight=100,
        groups=(
            NavMenuGroup(
                name="Tenancy",
                weight=300,
                items=(
                    NavMenuItem(
                        link="tenancy:tenant_list",
                        name="Tenants",
                        weight=100,
                        permissions=[
                            "tenancy.view_tenant",
                        ],
                        buttons=(
                            NavMenuAddButton(
                                link="tenancy:tenant_add",
                                permissions=[
                                    "tenancy.add_tag",
                                ],
                            ),
                            NavMenuImportButton(
                                link="tenancy:tenant_import",
                                permissions=[
                                    "tenancy.add_tenant",
                                ],
                            ),
                        ),
                    ),
                    NavMenuItem(
                        link="tenancy:tenantgroup_list",
                        name="Tenant Groups",
                        weight=200,
                        permissions=[
                            "tenancy.view_tenantgroup",
                        ],
                        buttons=(
                            NavMenuAddButton(
                                link="tenancy:tenantgroup_add",
                                permissions=[
                                    "tenancy.add_tenantgroup",
                                ],
                            ),
                            NavMenuImportButton(
                                link="tenancy:tenantgroup_import",
                                permissions=[
                                    "tenancy.add_tenantgroup",
                                ],
                            ),
                        ),
                    ),
                ),
            ),
        ),
    ),
)