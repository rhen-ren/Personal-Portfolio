from nicegui import ui, app
import asyncio
import time
import random

app.colors(primary="#39FF14")


async def typewriter(label: ui.label, message: str):
    label.set_text("")
    new_text: str = "> "
    delay: float = random.uniform(0.03, 0.04)

    for char in message:
        new_text += char
        label.set_text(new_text)
        await asyncio.sleep(delay)

async def intro_sequence(label1, label2, label3, tabs_container):
    await typewriter(label1, "Hello! My name is Efren Alano III")
    await typewriter(label2, "Backend Developer | Student")
    await typewriter(label3, "Welcome to my portfolio")
    tabs_container.set_visibility(True)

def projects():
    projects: list[dict] = [
        {"project_name": "Blogging-Platform-API", "description" : "A simple blogging platform API built using FastAPI and SQLAlchemy", "github_link": "https://github.com/rhen-ren/Blogging-Platform-API", "tags": ["RestAPI", "CRUD"]},
        {"project_name": "Todo-List-API", "github_link": "https://github.com/rhen-ren/Todo-List-API", "description": "A simple Todo API built with FastAPI and SQLAlchemy", "tags": ["RestAPI","CRUD", "ORM", "Auth"]}
    ]

    return projects

def sendEmail(name: str, email: str, message: str):
    ui.notify("Email Sent!")


@ui.page("/")
def home():
    # ui.query("body").style("margin: 40px; background-color: #0C100C")
    ui.add_css("""
        body{
        background-color: #0C100C;
        }

        body::after {
            content: "";
            position: fixed;
            inset: 0;
            pointer-events: none;
            z-index: 9999;

            background: repeating-linear-gradient(
                to bottom,
                transparent 0px,
                transparent 2px,
                rgba(0, 0, 0, 0.22) 3px,
                rgba(0, 0, 0, 0.22) 4px
            );
        }

        .retro-text {
            color: #00FF41;
            text-shadow:
                0 0 2px #00FF41,
                0 0 8px rgba(0, 255, 65, 0.5);
        }

        @keyframes crt-flicker {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.97; }
        }

        body {
            animation: crt-flicker 0.15s infinite;
        }

        body::before {
            content: "";
            position: fixed;
            inset: 0;
            pointer-events: none;
            z-index: 9998;
            background: radial-gradient(
                ellipse at center,
                transparent 55%,
                rgba(0, 0, 0, 0.4) 100%
            );
        }
    """)

    ui.add_css("""
        .intro{
            flex: 2;
            justify-content: center;
            align-items: left;
            padding-left: 30px;
        }
    """)

    ui.add_css("""
    .text-style-base{
        color: white;
        font-family: monospace;
        font-size: 16px;
        }
    .text-style-header{
        color: #39FF14;
        font-family: monospace;
        font-weight: bold;
        font-size: 24px;
    }

    .contact-input .q-field__control:before{
        border-color: white;
    }
    .contact-input .q-field__label{
        color:white;
        font-family: monospace;
    }
    .contact-input input{
        color: white;
        font-family: monospace;
    }

    .contact-text-area textarea{
        color: white;
    }
    .contact-text-area .q-field__control:before{
        border-color: white;
    }
    .contact-text-area .q-field__label{
        color: white;
    }
    """)

    intro_container = ui.row().style("width: 100%; justify-content: center; align-items: center; flex-wrap: wrap; padding: 40px")
    ui.separator().style("background-color: white; height: 2px; width: calc(100% - 60px); margin: auto")   
    tabs_container = ui.column().style("width: 100%; padding: 0px 40px 0px 40px;")
    tabs_container.set_visibility(False)

    with intro_container:
        ui.image("assets/me.png").style("width: 300px; flex-shrink: 0;")
        with ui.column().classes("intro"):
            intro_label1: ui.label = ui.label("").style("text-align: left; font-family: monospace; font-weight: bold; font-size: clamp(16px, 3vw, 32px); color: #00FF41; max-width: 700px;")
            intro_label2: ui.label = ui.label("").style("text-align: left; font-family: monospace; font-weight: bold; font-size: clamp(16px, 3vw, 32px); color: #00FF41; max-width: 700px;")
            intro_label3: ui.label = ui.label("").style("text-align: left; font-family: monospace; font-weight: bold; font-size: clamp(16px, 3vw, 32px); color: #00FF41; max-width: 700px;")
            asyncio.create_task(intro_sequence(intro_label1, intro_label2, intro_label3, tabs_container))

    with tabs_container:
        with ui.tabs() as tabs:
            about_tab = ui.tab("About").style("color: white; font-family: Lucida Console;")
            projects_tab = ui.tab("Projects").style("color: white; font-family: Lucida Console;")
            contact_tab = ui.tab("Contact").style("color: white; font-family: Lucida Console;")
        with ui.tab_panels(tabs, value=about_tab).style("width: 100%; background-color: #0C100C;"):
            with ui.tab_panel(about_tab):
                with ui.row().style(" width: 100%; flex-wrap: wrap;"):
                    with ui.column():
                        ui.label("Bachelor of Science in Information Technology").classes("text-style-base")
                        ui.label("Student at Polytechnic University of the Philippines").classes("text-style-base")
                        ui.label("Im an aspiring Backend Developer passionate building fast, reliable, and scalable server-side systems. My primary focus is designing clean RESTful APIs using modern Python tools, architecting relational databases, and applying clean coding principles.").classes("text-style-base")
                        ui.label("Skills").classes("text-style-header")

                with ui.row().style("width: 100%; flex-wrap: wrap;"):
                        with ui.column().style("max-width: 40%; min-width: 300px; flex: 1 1 50%"):
                            ui.label("Language and Database").classes("text-style-header")
                            ui.label("Python (Primary Language)").classes("text-style-base")
                            ui.label("PostgreSQL (Relational Database Design)").classes("text-style-base")

                            ui.label("Backend Framework & tools").classes("text-style-header")
                            ui.label("FastAPI (REST API Development)").classes("text-style-base")
                            ui.label("SQLAlchemy ORM (Database Management & Models)").classes("text-style-base")
                            ui.label("Pydantic (Data Validation)").classes("text-style-base")

                            ui.label("Testing & Quality Assurance").classes("text-style-header")
                            ui.label("Pytest (Integration Testing)").classes("text-style-base")

                            ui.label("Development Tools").classes("text-style-header")
                            ui.label("Git/Github (Version Control & Collaboration)").classes("text-style-base")
                            ui.label("Postman (API Endpoint Testing)").classes("text-style-base")
                            ui.label("Bash (Command-line Operations)").classes("text-style-base")

                            ui.label("Other / Academic Background").classes("text-style-header")
                            ui.label("Java & C# (Familiar)").classes("text-style-base")

                        with ui.column().style("flex: 1 1 0%;"):
                            with ui.row().style("width: 100%; border: 1px solid white; border-radius: 3px; justify-content: center; align-items: center;"):
                                ui.image("assets/python-original-wordmark.svg").style("width: 100px;")
                                ui.image("assets/postgresql-original-wordmark.svg").style("width: 100px;")
                                ui.image("assets/fastapi-original-wordmark.svg").style("width: 100px;")
                                ui.image("assets/sqlalchemy-original-wordmark.svg").style("width: 100px;")
                                ui.image("assets/pytest-original-wordmark.svg").style("width: 100px;")

                            ui.image("assets/winkingcow-highres.png").style("width: 100%")
            
            with ui.tab_panel(projects_tab):
                for proj in projects():
                    with ui.column().style(" width: 100%;"):
                        ui.label(f"> {proj["project_name"]}").classes("text-style-base").style("font-size: 25px; font-weight: bold")
                        ui.label(f"  {proj["description"]}").classes("text-style-base")

                        
                        with ui.row().style("width: 100%; flex-wrap: wrap;"):
                            for tag in proj["tags"]:
                                ui.label(tag).classes("text-style-base").style("width: 100px; border: 2px white solid; border-radius: 10px; text-align: center;")
    

                        with ui.link("GithubLink", proj["github_link"]).classes("text-style-base").style("color: white;"):
                            ui.icon("arrow_outward")

                        ui.separator().style("background-color: white; height: 1px;") 

            with ui.tab_panel(contact_tab):
                with ui.row().style("width: 100%; justify-content: center;"):

                    with ui.column().style("width: 50%"):
                        ui.label("Have a question or want to work together? Send me an email.").style("color: white; font-size: 20px; font-family: monospace;")
                        ui.label("Send me an email.").style("color: white; font-size: 20px; font-family: monospace;")

                        name: ui.input = ui.input(label="Your name").classes("contact-input").style("width: 100%;")
                        email: ui.input = ui.input(label="Your email").classes("contact-input").style("width: 100%;")
                        message: ui.textarea = ui.textarea("Your message").classes("contact-text-area").style("width: 100%;")
                        with ui.button(on_click=lambda: sendEmail(name, email, message) ).style("color: white;"):
                            ui.label("Send Email")
                            ui.icon("send")
                        

                         
                

ui.run()