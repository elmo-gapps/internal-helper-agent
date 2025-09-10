from mcp.server.fastmcp import FastMCP
import os
import requests
from typing import List, Dict, Any

# instantiate an MCP server client
mcp = FastMCP("Severa MCP Server")

BASE_URL = "https://api.severa.stag.visma.com/rest-api/v1.0"

# DEFINE TOOLS


def get_access_token() -> str:
    """
    Get an access token from Severa API.
    """
    client_id = os.getenv("SEVERA_CLIENT_ID")
    client_secret = os.getenv("SEVERA_CLIENT_SECRET")

    if not client_id or not client_secret:
        raise ValueError(
            "SEVERA_CLIENT_ID and SEVERA_CLIENT_SECRET environment variables are not set.")

    url = f"{BASE_URL}/token"
    data = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
        "scope": "customers:read projects:read invoices:read hours:read"
    }
    response = requests.post(url, data=data)
    response.raise_for_status()
    return response.json()["access_token"]


@mcp.tool()
def get_customers() -> List[Dict[str, Any]]:
    """
    Get all customers from Severa API.
    """
    access_token = get_access_token()
    url = f"{BASE_URL}/customers"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()


@mcp.tool()
def get_projects() -> List[Dict[str, Any]]:
    """
    Get all projects from Severa API.
    """
    access_token = get_access_token()
    url = f"{BASE_URL}/projects"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()


@mcp.tool()
def get_invoices() -> List[Dict[str, Any]]:
    """
    Get all invoices from Severa API.
    """
    access_token = get_access_token()
    url = f"{BASE_URL}/invoices"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()


@mcp.tool()
def get_work_hours() -> List[Dict[str, Any]]:
    """
    Get all work hours from Severa API.
    """
    access_token = get_access_token()
    url = f"{BASE_URL}/workhours"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()


 # execute and return the stdio output
if __name__ == "__main__":
    mcp.run()
