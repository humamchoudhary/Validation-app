from flet import (colors, AppBar, Text, Column,
                  ElevatedButton, Row, TextField, Container, alignment, padding, ButtonStyle, Image, image, IconButton, icons)
import flet

from flet.buttons import RoundedRectangleBorder
from credit import imei_validaiton, cc_validaiton
from isbn import isbn10_validation, isbn13_validation

BG_COLOR = colors.WHITE
PRIM_COLOR = colors.BLACK12
SEC_COLOR = colors.BLACK45
TXT_COLOR = colors.BLUE_ACCENT
APPBAR = AppBar(
    center_title=True,
    bgcolor=PRIM_COLOR,
    actions=[],
)


def Navigator(page):
    page.appbar = APPBAR
    page.bgcolor = PRIM_COLOR
    page.title = ""
    page.vertical_alignment = "center"
    main_page(page)


def main_page(page):
    def cc_route(e):
        card_val_page((page))

    def isbn10_route(e):
        isbn10_page((page))

    def isbn13_route(e):
        isbn13_page((page))

    def imei_route(e):
        imei_val_page((page))
    page.clean()

    def back(e):
        main_page(page)
    APPBAR.leading = IconButton(
        icon=icons.ARROW_BACK,
        on_click=back
    )
    APPBAR.title = Text("Validation App")
    cc_btn = ElevatedButton("Credit Card Validation", color=TXT_COLOR, on_click=cc_route,
                            style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)))
    imei_btn = ElevatedButton("IMEI Validation", color=TXT_COLOR, on_click=imei_route,
                              style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)))
    isbn10_btn = ElevatedButton("ISBN-10 Validation", color=TXT_COLOR, on_click=isbn10_route,
                                style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)))
    isbn13_btn = ElevatedButton("ISBN-13 Validation",  color=TXT_COLOR, on_click=isbn13_route,
                                style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)))
    page.add(Column([
        Row([
            cc_btn,
            imei_btn,
            isbn10_btn,
            isbn13_btn
        ], alignment="center")
    ], alignment="center"))


def isbn13_page(page):
    def submit(e):
        cc_in.error_text = None
        confirmation_txt.value = None
        if cc_in.value:
            if isbn13_validation(str(cc_in.value)):
                confirmation_txt.value = "The isbn-13 is valid"
                cc_in.error_text = None
            else:
                cc_in.error_text = "Invalid isbn-13 try again!"

        else:
            cc_in.error_text = "Please enter a isbn-13 number"
        page.update()

    page.clean()
    APPBAR.title = Text("ISBN-13 Validation")

    cc_label = Text("Enter ISBN-13 Number: ", color=TXT_COLOR)
    cc_in = TextField(label="", color=TXT_COLOR, border_color=TXT_COLOR, focused_color=TXT_COLOR, width=400,
                            focused_border_color=TXT_COLOR, focused_bgcolor="white", selection_color="white")
    confirmation_txt = Text(value="", color="green")
    submit_btn = ElevatedButton(
        "Submit", width=100, height=50, color=TXT_COLOR, on_click=submit, style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)))
    container = Container(content=Column([
        Row([confirmation_txt], alignment="center"),
        cc_label,
        Row([
            cc_in,
            submit_btn
        ], tight=True
        )
    ], tight=True),
        expand=False,
        # width=580,

        bgcolor=SEC_COLOR,
        padding=padding.only(top=20, bottom=20, left=20, right=20),
        alignment=alignment.center,
        border_radius=7
    )

    page.add(Row([container], alignment='center'))


def isbn10_page(page):
    def submit(e):
        cc_in.error_text = None
        confirmation_txt.value = None
        if cc_in.value:
            if isbn10_validation(str(cc_in.value)):
                confirmation_txt.value = "The isbn-10 is valid"
                cc_in.error_text = None
            else:
                cc_in.error_text = "Invalid isbn-10 try again!"

        else:
            cc_in.error_text = "Please enter a isbn-10 number"
        page.update()

    page.clean()
    APPBAR.title = Text("ISBN-10 Validation")

    cc_label = Text("Enter ISBN-10 Number: ", color=TXT_COLOR)
    cc_in = TextField(label="", color=TXT_COLOR, border_color=TXT_COLOR, focused_color=TXT_COLOR, width=400,
                            focused_border_color=TXT_COLOR, focused_bgcolor="white", selection_color="white")
    confirmation_txt = Text(value="", color="green")
    submit_btn = ElevatedButton(
        "Submit", width=100, height=50, color=TXT_COLOR, on_click=submit, style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)))
    container = Container(content=Column([
        Row([confirmation_txt], alignment="center"),
        cc_label,
        Row([
            cc_in,
            submit_btn
        ], tight=True
        )
    ], tight=True),
        expand=False,
        # width=580,

        bgcolor=SEC_COLOR,
        padding=padding.only(top=20, bottom=20, left=20, right=20),
        alignment=alignment.center,
        border_radius=7
    )

    page.add(Row([container], alignment='center'))


def card_val_page(page):
    def submit(e):
        cc_in.error_text = None
        confirmation_txt.value = None

        if cc_in.value:
            if cc_validaiton(int(cc_in.value)):
                confirmation_txt.value = "The card is valid"
                cc_in.error_text = None
            else:
                cc_in.error_text = "Invalid card try again!"

        else:
            cc_in.error_text = "Please enter a card number fields"
        page.update()

    page.clean()

    APPBAR.title = Text("Credit Card Validation")

    imc = Container(content=Image(
        src="vc.png",
        # fit="contain",
    ), width=120, height=80)
    cc_label = Text("Enter Credit Card Number: ", color=TXT_COLOR)
    cc_in = TextField(label="", color=TXT_COLOR, border_color=TXT_COLOR, focused_color=TXT_COLOR, width=400,
                            focused_border_color=TXT_COLOR, focused_bgcolor="white", selection_color="white")
    confirmation_txt = Text(value="", color="green")
    submit_btn = ElevatedButton(
        "Submit", width=100, height=50, color=TXT_COLOR, on_click=submit, style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)))
    container = Container(content=Column([
        Row([confirmation_txt], alignment="center"),
        cc_label,
        Row([
            cc_in, imc,
            submit_btn
        ], tight=True
        )
    ], tight=True),
        expand=False,
        # width=580,

        bgcolor=SEC_COLOR,
        padding=padding.only(top=20, bottom=20, left=20, right=20),
        alignment=alignment.center,
        border_radius=7
    )

    page.add(Row([container], alignment='center'))


def imei_val_page(page):
    def submit(e):
        cc_in.error_text = None
        confirmation_txt.value = None

        if cc_in.value:
            if imei_validaiton(int(cc_in.value)):
                confirmation_txt.value = "The IMEI is valid"
                cc_in.error_text = None
            else:
                cc_in.error_text = "Invalid IMEI try again!"

        else:
            cc_in.error_text = "Please enter a IMEI number"
        page.update()

    page.clean()

    APPBAR.title = Text("IMEI Validation")

    imc = Container(content=Image(
        src="vc.png",
        # fit="contain",
    ), width=120, height=80)
    cc_label = Text("Enter IMEI Number: ", color=TXT_COLOR)
    cc_in = TextField(label="", color=TXT_COLOR, border_color=TXT_COLOR, focused_color=TXT_COLOR, width=400,
                            focused_border_color=TXT_COLOR, focused_bgcolor="white", selection_color="white")
    confirmation_txt = Text(value="", color="green")
    submit_btn = ElevatedButton(
        "Submit", width=100, height=50, color=TXT_COLOR, on_click=submit, style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)))
    container = Container(content=Column([
        Row([confirmation_txt], alignment="center"),
        cc_label,
        Row([
            cc_in, imc,
            submit_btn
        ], tight=True
        )
    ], tight=True),
        expand=False,
        # width=580,

        bgcolor=SEC_COLOR,
        padding=padding.only(top=20, bottom=20, left=20, right=20),
        alignment=alignment.center,
        border_radius=7
    )

    page.add(Row([container], alignment='center'))


if __name__ == "__main__":
    flet.app(target=Navigator)
