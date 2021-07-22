from dearpygui.dearpygui import *
from dearpygui.demo import *
import requests
import platform


vp = create_viewport(title='Window', width=1180, height=750, y_pos=0, x_pos=0)
setup_dearpygui(viewport=vp)
show_viewport(vp)

lightblue = "51B7FF"
orange = "FFC250"
purple = "7E49F0"
blue = "4A8FEE"
green = "4AEC86"
yellow = "DEEE4A"


with theme() as search_bar:
    add_theme_color(mvThemeCol_FrameBg, (78,78,78,255), category= mvThemeCat_Core)
    add_theme_style(mvStyleVar_FrameRounding, 10, category= mvThemeCat_Core)
    add_theme_style(mvStyleVar_FramePadding, 20, 15, category= mvThemeCat_Core)


with theme() as light_blue_theme:
    add_theme_color(mvThemeCol_ChildBg, (81,183,255), category= mvThemeCat_Core)
    add_theme_style(mvStyleVar_ItemSpacing, 40, 10, category= mvThemeCat_Core)

with theme() as orange_theme:
    add_theme_color(mvThemeCol_ChildBg, (255,194,80), category= mvThemeCat_Core)
    add_theme_style(mvStyleVar_ItemSpacing, 40, 10, category= mvThemeCat_Core)

with theme() as purple_theme:
    add_theme_color(mvThemeCol_ChildBg, (126,73,240), category= mvThemeCat_Core)
    add_theme_style(mvStyleVar_ItemSpacing, 40, 10, category= mvThemeCat_Core)

with theme() as blue_theme:
    add_theme_color(mvThemeCol_ChildBg, (74,143,238), category= mvThemeCat_Core)
    add_theme_style(mvStyleVar_ItemSpacing, 40, 10, category= mvThemeCat_Core)

with theme() as green_theme:
    add_theme_color(mvThemeCol_ChildBg, (74,236,134), category= mvThemeCat_Core)
    add_theme_style(mvStyleVar_ItemSpacing, 40, 10, category= mvThemeCat_Core)

with theme() as yellow_theme:
    add_theme_color(mvThemeCol_ChildBg, (222,238,74), category= mvThemeCat_Core)
    add_theme_style(mvStyleVar_ItemSpacing, 40, 10, category= mvThemeCat_Core)

with theme() as most_viewed_theme:
    add_theme_style(mvStyleVar_ItemSpacing, 10, 40, category= mvThemeCat_Core)


with theme(default_theme=True) as theme_custom:
    add_theme_color(mvThemeCol_WindowBg, (39, 37, 55, 255), category= mvThemeCat_Core)
    add_theme_color(mvThemeCol_FrameBg, (39, 37, 55, 255), category= mvThemeCat_Core)
    add_theme_color(mvThemeCol_Header, (28,28,42,255), category= mvThemeCat_Core)
    add_theme_color(mvThemeCol_HeaderHovered, (64,60,80,103), category= mvThemeCat_Core)


    add_theme_style(mvStyleVar_FrameRounding, 10, category= mvThemeCat_Core)
    add_theme_style(mvStyleVar_ChildRounding, 20, category= mvThemeCat_Core)
    add_theme_style(mvStyleVar_FramePadding, 20, 5, category= mvThemeCat_Core)
    add_theme_style(mvStyleVar_WindowPadding, 20, 20, category= mvThemeCat_Core)
    add_theme_style(mvStyleVar_ItemSpacing, 30, 30, category= mvThemeCat_Core)
    add_theme_style(mvStyleVar_ItemInnerSpacing, 20, 20, category= mvThemeCat_Core)


def set_theme_custom():
    set_item_font(title, roboto_thin)
    set_item_font(discover_text, roboto_thin)
    set_item_font(world_leader, roboto_bold)
    set_item_font(world_leader2, roboto_bold)




class Tabs:
    current_tab=0


with font_registry():

    add_font("Roboto-Light.ttf", 20, default_font=True)
    roboto_thin = add_font("Roboto-Light.ttf", 35)
    roboto_bold = add_font("Roboto-Bold.ttf", 35)
    roboto_thin_large = add_font("Roboto-Light.ttf", 45)



uname = platform.uname()
height_d = 1080
width_d = 1920

class Credentials():
    response = ""
    token = ""

def get_sizes():
    print("lol")

def resizeme():
    print("resized")

def manager(to_show, to_hide):
    configure_item(to_show, show = True)
    configure_item(to_hide, show = False)

def login():
    us = get_value(username_in)
    passw = get_value(password_in)
    if us == "" and passw == "":
        configure_item(status, default_value="Fields empty.")
        return
    else:
        pass 
    if us == "":
        configure_item(status, default_value="Fill in the username.")
        #show empty username
        return
    else:
        pass
    if passw == "":
        configure_item(status, default_value="Fill in the password.")
        #show empty password
        return
    else:
        pass
    url = "http://127.0.0.1:8000/api-token-auth/"
    url_verify = "http://127.0.0.1:8000/hello/"
    payload = {
        'username': f'{us}',
        'password': f'{passw}'
    }
    r = requests.post(url, data=payload)
    Credentials.response = r.json()
    if Credentials.response == {'non_field_errors': ['Unable to log in with provided credentials.']}:
        configure_item(status, default_value="Invalid login.")
        return
        #show invalid
    else:
        pass
    Credentials.token = Credentials.response['token']

    headers = {"Authorization" :f"Token {Credentials.token}"}
    r2 = requests.get(url_verify, headers=headers)

    if r2.json() == {'detail': 'Invalid token.'}:
        configure_item(status, default_value="Invalid login.")
        #show invalid

    if r2.json() == {'message': 'Hello, world!'}:
        configure_item(status, default_value="Logged in.")
        manager(postlog, prelogin)
        #move on to another page
    else:
        configure_item(status, default_value="Invalid login.")


def manager(to_show, to_hide):
    configure_item(to_show, show = True)
    configure_item(to_hide, show = False)

with window(show=False, no_bring_to_front_on_focus=True) as postlog:
    lol = add_text(default_value="System information")
    add_text(default_value=f"{uname.system}")
    add_text(default_value=f"{uname.node}")
    add_text(default_value=f"{uname.release}")
    add_text(default_value=f"{uname.version}")
    add_text(default_value=f"{uname.machine}")
    add_text(default_value=f"{uname.processor}")

with window(no_title_bar=True, no_resize=True, no_move = True, show=False) as prelogin:
    add_text("Login window")
    username_in = add_input_text(label="Username")
    password_in = add_input_text(label="Password")
    add_button(label="Submit", callback=login)
    status = add_text(default_value="")

    test_button = add_button(label="Update", callback= lambda: manager(postlog, prelogin))

with window(no_title_bar=True, no_resize=True, no_move = True) as modern:

    with group() as left_group:
        title = add_text("Elixir")
        tabs = add_listbox(items=["Home", "Discover", "Featured"], label="", num_items=3, width=300)
    add_same_line()

    with group() as right_group:

        search_bar_widget = add_input_text(label="", hint="Search", width=300)

        with group() as discover:
            discover_text = add_text("Discover")
            with child(width=450, height=250) as light_blue:
                world_leader = add_text(f"World leader")
                world_leader2 = add_text(f"in global finance")
                add_text(f"Get started today!")
            
            add_same_line()

            with child(width=250, height=250) as orange:
                add_text(f"")

        with group() as most_watched:
            most_viewed_text = add_text("Most Watched")

            with child(width=175, height=175) as purple:
                add_text(f"")
            add_same_line()
            with child(width=175, height=175) as blue:
                add_text(f"")
            add_same_line()
            with child(width=175, height=175) as green:
                add_text(f"")
            add_same_line()
            with child(width=175, height=175) as yellow:
                add_text(f"")

show_style_editor()
set_theme_custom()
set_item_theme(search_bar_widget, search_bar)
set_item_theme(light_blue, light_blue_theme)
set_item_theme(orange, orange_theme)
set_item_theme(purple, purple_theme)
set_item_theme(blue, blue_theme)
set_item_theme(green, green_theme)
set_item_theme(yellow, yellow_theme)
set_item_theme(most_watched, most_viewed_theme)
set_primary_window(modern, True)
start_dearpygui()
