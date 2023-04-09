import typer
from split_service import split
import json

main = typer.Typer()

@main.command()
def hello(name: str, verbose: bool=False):
    print(f"Hello, {name}!")

    if verbose: 
        print("Program finished.")

@main.command(name="list-all")
def list_all(environments:dict):
    response_json = split.list_all_splits()
    print(json.dumps(response_json, indent=4, sort_keys=True))

# @main.command(name="update-split", )
# def update_split(name:str, org:str, body:str, environments:dict):
#     response_json = split.update_split().json()
#     print(json.dumps(response_json, indent=4, sort_keys=True))

# @main.command(name="update-description")
# def update_desc(name:str, org:str, body:str, environments:dict):
#     response_json = split.update_description().json()
#     print(json.dumps(response_json, indent=4, sort_keys=True))

# @main.command(name="new-split")
# def add_new(name:str, org:str, body:str, environments:dict):
#     response_json = split.create_split().json()
#     print(json.dumps(response_json, indent=4, sort_keys=True))




if __name__ == "__main__":
    main()