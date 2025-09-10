# ADK Agents

This document provides technical documentation for the ADK Agents project, an AI assistant designed to interact with multiple services like HubSpot and Severa.

## Overview

This project implements a multi-agent system using the Agent Development Kit (ADK). The main assistant can delegate tasks to specialized agents for HubSpot and Severa.

## Agents

### HubSpot Specialist

The HubSpot Specialist is an AI assistant that helps users manage their HubSpot CRM. It is an expert in managing contacts, deals, and companies, and can answer questions using real-time data from HubSpot by using its tools.

#### Core Capabilities

-   **CRM Management**: Create, retrieve, update, and delete contacts, companies, and deals.
-   **Information Retrieval**: Answer questions using real-time data from HubSpot.
-   **Summarization**: Provide summaries of sales pipelines or marketing campaign performance.

#### Available Tools

-   `get_all_contacts()`: Retrieves a list of all contacts from HubSpot.
-   `get_all_companies()`: Retrieves a list of all companies from HubSpot.
-   `get_all_deals()`: Retrieves a list of all deals from HubSpot.
-   `create_contact(email: str, firstname: str, lastname: str, ...)`: Creates a new contact.
-   `create_company(name: str, domain: str, ...)`: Creates a new company.
-   `search_contacts_by_company(company_name: str)`: Searches for contacts associated with a specific company name.
-   `search_companies_by_name(company_name: str)`: Searches for companies by name.
-   `search_deals_by_name(deal_name: str)`: Searches for deals by name.

### Severa Specialist

The Severa Specialist is an AI assistant that helps users with their Severa project management and billing. It is an expert in managing customers, projects, invoices, and work hours.

#### Core Capabilities

-   **CRM & Project Management**: Manage customers, projects, invoices, and work hours.
-   **Information Retrieval**: Answer questions using real-time data from Severa.

#### Available Tools

-   `get_customers()`: Retrieves a list of all customers from Severa.
-   `get_projects()`: Retrieves a list of all projects from Severa.
-   `get_invoices()`: Retrieves a list of all invoices from Severa.
-   `get_work_hours()`: Retrieves work hour entries.

## Setup and Installation

To get the agent up and running, follow these steps:

1.  **Prerequisites**: Ensure you have Python 3.x installed.
2.  **Install Dependencies**: Install the required packages using the `requirements.txt` file:
    ```bash
    pip install -r requirements.txt
    ```
3.  **Configuration**: The agent requires access tokens to authenticate with the APIs. Set the following environment variables:
    ```bash
    export HUBSPOT_ACCESS_TOKEN="your-hubspot-access-token"
    export SEVERA_CLIENT_ID="your-severa-client-id"
    export SEVERA_CLIENT_SECRET="your-severa-client-secret"
    ```

## Running the Application

To run the agent, use the `adk` command-line tool:

```bash
adk run assistant-agent
```
