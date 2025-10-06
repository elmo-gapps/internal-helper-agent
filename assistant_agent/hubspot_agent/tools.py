import os
import hubspot
from hubspot.crm.contacts.models.public_object_search_request import (
    PublicObjectSearchRequest,
)

# Use the access token from environment variables
api_client = hubspot.HubSpot(access_token=os.getenv("HUBSPOT_ACCESS_TOKEN"))


def get_all_contacts() -> dict:
    """
    Retrieves all contacts from HubSpot.
    """
    return api_client.crm.contacts.basic_api.get_page().to_dict()


def get_all_companies() -> dict:
    """
    Retrieves all companies from HubSpot.
    """
    return api_client.crm.companies.basic_api.get_page().to_dict()


def get_all_deals() -> dict:
    """
    Retrieve all deals from HubSpot.
    """
    return api_client.crm.deals.basic_api.get_page().to_dict()


def get_all_leads() -> dict:
    """
    Retrieves all leads from HubSpot. A lead is a contact with lifecyclestage='lead'.
    """
    search_request = PublicObjectSearchRequest(
        filter_groups=[
            {
                "filters": [
                    {
                        "propertyName": "lifecyclestage",
                        "operator": "EQ",
                        "value": "lead",
                    }
                ]
            }
        ]
    )
    return api_client.crm.contacts.search_api.do_search(
        public_object_search_request=search_request
    ).to_dict()


def search_contacts_by_company(company_name: str) -> dict:
    """
    Searches for contacts by company name.
    :param company_name: The name of the company to search for contacts in.
    :return: A list of contacts from that company.
    """
    search_request = PublicObjectSearchRequest(
        filter_groups=[
            {
                "filters": [
                    {
                        "propertyName": "company",
                        "operator": "CONTAINS_TOKEN",
                        "value": company_name,
                    }
                ]
            }
        ]
    )
    return api_client.crm.contacts.search_api.do_search(
        public_object_search_request=search_request
    ).to_dict()


def search_companies_by_name(company_name: str) -> dict:
    """
    Searches for companies by name.
    :param company_name: The name of the company to search for.
    :return: A list of companies with that name.
    """
    search_request = PublicObjectSearchRequest(
        filter_groups=[
            {
                "filters": [
                    {
                        "propertyName": "name",
                        "operator": "CONTAINS_TOKEN",
                        "value": company_name,
                    }
                ]
            }
        ]
    )
    return api_client.crm.companies.search_api.do_search(
        public_object_search_request=search_request
    ).to_dict()


def search_deals_by_name(deal_name: str) -> dict:
    """
    Searches for deals by name.
    :param deal_name: The name of the deal to search for.
    :return: A list of deals with that name.
    """
    search_request = PublicObjectSearchRequest(
        filter_groups=[
            {
                "filters": [
                    {
                        "propertyName": "dealname",
                        "operator": "CONTAINS_TOKEN",
                        "value": deal_name,
                    }
                ]
            }
        ]
    )
    return api_client.crm.deals.search_api.do_search(
        public_object_search_request=search_request
    ).to_dict()


def search_leads_by_name(lead_name: str) -> dict:
    """
    Searches for leads by name. A lead is a contact with lifecyclestage='lead'.
    The search is performed on both firstname and lastname.
    :param lead_name: The name of the lead to search for.
    :return: A list of leads with that name.
    """
    search_request = PublicObjectSearchRequest(
        filter_groups=[
            {
                "filters": [
                    {"propertyName": "lifecyclestage",
                        "operator": "EQ", "value": "lead"},
                    {
                        "propertyName": "firstname",
                        "operator": "CONTAINS_TOKEN",
                        "value": lead_name,
                    },
                ]
            },
            {
                "filters": [
                    {"propertyName": "lifecyclestage",
                        "operator": "EQ", "value": "lead"},
                    {
                        "propertyName": "lastname",
                        "operator": "CONTAINS_TOKEN",
                        "value": lead_name,
                    },
                ]
            },
        ]
    )
    return api_client.crm.contacts.search_api.do_search(
        public_object_search_request=search_request
    ).to_dict()


def create_contact(
    email: str,
    firstname: str,
    lastname: str,
    phone: str,
    company: str,
    website: str = "",
    lifecyclestage: str = "",
) -> dict:
    """
    Creates a new contact in HubSpot.
    :param email: The contact's email address.
    :param firstname: The contact's first name.
    :param lastname: The contact's last name.
    :param phone: The contact's phone number.
    :param company: The contact's company name.
    :param website: The contact's website. (Optional)
    :param lifecyclestage: The contact's lifecycle stage. (Optional)
    :return: The created contact's details.
    """
    properties = {
        "email": email,
        "firstname": firstname,
        "lastname": lastname,
        "phone": phone,
        "company": company,
        "website": website,
        "lifecyclestage": lifecyclestage,
    }
    # Filter out None values
    contact_data = {"properties": {k: v for k,
                                   v in properties.items() if v is not ""}}
    return api_client.crm.contacts.basic_api.create(
        simple_public_object_input_for_create=contact_data
    ).to_dict()


def create_company(
    name: str,
    domain: str,
    city: str = "",
    industry: str = "",
    phone: str = "",
    state: str = "",
    lifecyclestage: str = "",
) -> dict:
    """
    Creates a new company in HubSpot.
    :param name: The company's name.
    :param domain: The company's domain.
    :param city: The company's city.
    :param industry: The company's industry.
    :param phone: The company's phone number.
    :param state: The company's state.
    :param lifecyclestage: The company's lifecycle stage.
    :return: The created company's details.
    """
    properties = {
        "name": name,
        "domain": domain,
        "city": city,
        "industry": industry,
        "phone": phone,
        "state": state,
        "lifecyclestage": lifecyclestage,
    }
    # Filter out None values
    company_data = {"properties": {k: v for k,
                                   v in properties.items() if v is not ""}}
    return api_client.crm.companies.basic_api.create(
        simple_public_object_input_for_create=company_data
    ).to_dict()
