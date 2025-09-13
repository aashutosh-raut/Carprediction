# from dash import html, dcc
# # import dash_table
# import pandas as pd
# import pickle
# import numpy as np


# df = pd.read_csv("Cars.csv")    # reading csv file using pandas

# filename = 'model/carPricePrediction.model' # importing pre-trained model carPricePrediction.model
# loaded_model = pickle.load(open(filename, 'rb'))    # loading trained model to loaded_model variable

# layout = html.Div(children=[    #creating main app layout and using its children class as subclass
#     html.H1(children='Welcome to Machine Learning'), # Main heading h1

#     html.H2(children='Car Price Prediction: Version 1'),

#     # html.Div([
#     #     html.Button('V1',id='v1'),
#     #     html.Button('V2',id='v2')
#     # ],style={'margin-bottom': '1rem'}),

    

#     html.Div("Car Price Prediction (CPP): A web application framework for predicting Car Prices."), # creating div


#     html.Div([  # creating button inside div to easily work with UI providing style
#         html.Button("DataFrame", id="dataFrame",
#                     style={"background-color": "blue", "color": "white", "padding": "10px",
#                         "border-radius": "10px", "margin-right": '10px', "cursor": "pointer","height": "40px"}),

#         html.Button("Instructions", id="instruction",
#                     style={"background-color": "blue", "color": "white", "padding": "10px",
#                         "border-radius": "10px", "cursor": "pointer","height": "40px"}),
#     ],style={"display": "flex","justify-content":"space-between","margin-top": "10px"}),

#     html.Div(id="table-container"),
#     dcc.Store(id="table-visible", data=False),  # using dash core component (dcc) for component to store data to browser
    
#     html.Div(id="instruction-container"),
#     dcc.Store(id="instruction-visible", data=False),  
    
#     html.Div([
#     html.Div([
#     html.Label(["Car Brand Name:"],style={"fontWeight": "bold"}),   # using label for dropdown 
#     dcc.Dropdown(
#         id="brand-input",
#         options=[   # Provided with Brand names and value as per LabelEncoder in A_Z ascending order
#             {"label": "Ambassador", "value": 0},
#             {"label": "Ashok", "value": 1},
#             {"label": "Audi", "value": 2},
#             {"label": "BMW", "value": 3},
#             {"label": "Chevrolet", "value": 4},
#             {"label": "Daewoo", "value": 5},
#             {"label": "Datsun", "value": 6},
#             {"label": "Fiat", "value": 7},
#             {"label": "Force", "value": 8},
#             {"label": "Ford", "value": 9},
#             {"label": "Honda", "value": 10},
#             {"label": "Hyundai", "value": 11},
#             {"label": "Isuzu", "value": 12},
#             {"label": "Jaguar", "value": 13},
#             {"label": "Jeep", "value": 14},
#             {"label": "Kia", "value": 15},
#             {"label": "Land", "value": 16},
#             {"label": "Lexus", "value": 17},
#             {"label": "MG", "value": 18},
#             {"label": "Mahindra", "value": 19},
#             {"label": "Maruti", "value": 20},
#             {"label": "Mercedes-Benz", "value": 21},
#             {"label": "Mitsubishi", "value": 22},
#             {"label": "Nissan", "value": 23},
#             {"label": "Opel", "value": 24},
#             {"label": "Peugeot", "value": 25},
#             {"label": "Renault", "value": 26},
#             {"label": "Skoda", "value": 27},
#             {"label": "Tata", "value": 28},
#             {"label": "Toyota", "value": 29},
#             {"label": "Volkswagen", "value": 30},
#             {"label": "Volvo", "value": 31}
#         ],
#         placeholder="Select Brand",
#         style={"margin-bottom": "10px","width": "22rem"}
#         ),
#     ],style={"margin-top": "1rem"}),
    
#     html.Div([
#         html.Label(["Kms Driven:"],style={"fontWeight": "bold"}),
#         dcc.Input(id="km", type="number", placeholder="Enter Km driven by Car", debounce=True,
#                   style={"margin-bottom": "10px", "display": "block","width": "22rem","padding": "6px"}),
#     ]),

#     html.Div([
#         html.Label(["Fuel Type:"],style={"fontWeight": "bold"}),
#         dcc.Dropdown(
#             id="fuel-input",
#             options=[
#             {"label": "Diesel", "value": 0},
#             {"label": "Petrol", "value": 1}
#             ],
#             placeholder="Select fuel",
#             style={"margin-bottom": "10px","width": "22rem"}
#         ),
#     ]),

#     html.Div([
#         html.Label(["Seller Type:"],style={"fontWeight": "bold"}),
#         dcc.Dropdown(
#             id="seller-type-input",  
#             options=[
#             {"label": "Dealer", "value": 0},
#             {"label": "Individual", "value": 1},
#             {"label": "Trustmark Dealer", "value": 2}
#             ],
#             placeholder="Select Seller Type",
#             style={"margin-bottom": "10px","width": "22rem"}
#         ),
#     ]),

#     html.Label(["Mileage (kmpl):"],style={"fontWeight": "bold"}),
#     dcc.Input(id="mileage", type="number", placeholder="Enter mileage", debounce=True,  # debounce to not run after each and everytime user make slight change in input space
#                 style={"margin-bottom": "10px", "display": "block","width": "22rem","padding": "6px"}),     # Taking user input and passing to app callback through id

#     html.Label(["Engine (CC):"],style={"fontWeight": "bold"}),
#     dcc.Input(id="engine", type="number", placeholder="Enter engine capacity", debounce=True,
#                 style={"margin-bottom": "10px", "display": "block","width": "22rem","padding": "6px"}),

#     html.Label(["Seats/Capacity:"],style={"fontWeight": "bold"}),
#     dcc.Input(id="seats", type="number", placeholder="Enter number of seats", debounce=True,
#                 style={"margin-bottom": "10px", "display": "block","width": "22rem","padding": "6px"}),

#     html.Label(["Max Power (bhp):"],style={"fontWeight": "bold"}),
#     dcc.Input(id="max_power", type="number", placeholder="Enter max power", debounce=True,
#                 style={"margin-bottom": "10px", "display": "block","width": "22rem","padding": "6px"}),
#     ],style={"margin-left": "0.2rem"}),
#     html.Button("Predict", id="prediction",
#                 style={"background-color": "blue", "color": "white", "padding": "10px",
#                        "border-radius": "10px", "cursor": "pointer" }),

#     html.Div(id="prediction-container"),
#     dcc.Store(id="prediction-visible", data=False)
# ], style={"padding": "1rem"})



from dash import html, dcc

button_style = {
    "background-color": "#007BFF",
    "color": "white",
    "padding": "10px 20px",
    "border-radius": "8px",
    "cursor": "pointer",
    "font-size": "16px",
    "border": "none",
    "margin": "5px"
}

input_style = {
    "width": "100%",
    "padding": "8px",
    "border-radius": "6px",
    "border": "1px solid #ccc",
    "margin-bottom": "10px"
}

layout = html.Div([
    html.H1("Car Price Prediction", style={"textAlign": "center", "color": "#333"}),

    html.Div([
        html.Button("Show DataFrame", id="dataFrame", style=button_style),
        html.Button("Instructions", id="instruction", style=button_style)
    ], style={"display": "flex", "justify-content": "center", "margin-bottom": "20px"}),

    html.Div(id="table-container"),
    dcc.Store(id="table-visible", data=False),

    html.Div(id="instruction-container"),
    dcc.Store(id="instruction-visible", data=False),

    html.H3("Enter Car Details", style={"margin-top": "20px", "color": "#555"}),

    html.Div([
        html.Div([
            html.Label("Car Brand Name", style={"fontWeight": "bold"}),
            dcc.Dropdown(
                id="brand-input",
                options=[{"label": x, "value": i} for i, x in enumerate(
                    ["Ambassador", "Ashok", "Audi", "BMW", "Chevrolet", "Daewoo",
                     "Datsun", "Fiat", "Force", "Ford", "Honda", "Hyundai", "Isuzu",
                     "Jaguar", "Jeep", "Kia", "Land", "Lexus", "MG", "Mahindra",
                     "Maruti", "Mercedes-Benz", "Mitsubishi", "Nissan", "Opel",
                     "Peugeot", "Renault", "Skoda", "Tata", "Toyota", "Volkswagen", "Volvo"]
                )],
                placeholder="Select Brand",
                style=input_style
            ),
        ], style={"flex": 1, "margin-right": "10px"}),

        html.Div([
            html.Label("Kms Driven", style={"fontWeight": "bold"}),
            dcc.Input(id="km", type="number", placeholder="Enter Km driven by Car", style=input_style),
        ], style={"flex": 1, "margin-left": "10px"}),
    ], style={"display": "flex", "gap": "20px"}),

    html.Div([
        html.Div([
            html.Label("Fuel Type", style={"fontWeight": "bold"}),
            dcc.Dropdown(
                id="fuel-input",
                options=[
                    {"label": "Diesel", "value": 0},
                    {"label": "Petrol", "value": 1}
                ],
                placeholder="Select Fuel Type",
                style=input_style
            ),
        ], style={"flex": 1, "margin-right": "10px"}),

        html.Div([
            html.Label("Seller Type", style={"fontWeight": "bold"}),
            dcc.Dropdown(
                id="seller-type-input",
                options=[
                    {"label": "Dealer", "value": 0},
                    {"label": "Individual", "value": 1},
                    {"label": "Trustmark Dealer", "value": 2}
                ],
                placeholder="Select Seller Type",
                style=input_style
            ),
        ], style={"flex": 1, "margin-left": "10px"}),
    ], style={"display": "flex", "gap": "20px"}),

    html.Div([
        html.Label("Mileage (kmpl)", style={"fontWeight": "bold"}),
        dcc.Input(id="mileage", type="number", placeholder="Enter mileage", style=input_style),
    ]),

    html.Div([
        html.Label("Engine (CC)", style={"fontWeight": "bold"}),
        dcc.Input(id="engine", type="number", placeholder="Enter engine capacity", style=input_style),
    ]),

    html.Div([
        html.Label("Seats/Capacity", style={"fontWeight": "bold"}),
        dcc.Input(id="seats", type="number", placeholder="Enter number of seats", style=input_style),
    ]),

    html.Div([
        html.Label("Max Power (bhp)", style={"fontWeight": "bold"}),
        dcc.Input(id="max_power", type="number", placeholder="Enter max power", style=input_style),
    ]),

    html.Button("Predict", id="prediction", style=button_style),

    html.Div(id="prediction-container",
             style={"margin-top": "20px", "font-size": "18px", "color": "#007BFF", "textAlign": "center"}),

    dcc.Store(id="prediction-visible", data=False)
], style={"max-width": "800px", "margin": "auto", "padding": "20px"})
