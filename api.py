from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# Use standard SymPy functions and symbols
from sympy import integrate, diff, solve, simplify, parse_expr, symbols

# Initialize FastAPI application
app = FastAPI()

# CORS configuration
origins = [
    "https://flutter-flow--sparkess145.replit.app", # Placeholder/Old link
    "*", # Allow all origins temporarily for testing
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Scientific Calculator Backend is running (Permanent Deployment)."}

@app.post("/calculate")
def calculate_expression(expression: str, operation: str = None, variable: str = 'x'):
    """
    Handles mathematical operations using SymPy.
    """
    try:
        # 1. Define the variable as a SymPy symbol (e.g., if variable='x', then x is a symbol)
        sym_var = symbols(variable)
        
        # 2. Safely parse the input string into a SymPy expression
        parsed_expression = parse_expr(expression)
        
        # 3. Apply the requested operation
        
        # Solving
        if operation == "solve":
            # Solves the expression equal to zero for the specified variable
            result = solve(parsed_expression, sym_var)
        
        # Integration
        elif operation == "integral":
            result = integrate(parsed_expression, sym_var)
            
        # Differentiation
        elif operation == "derivative":
            result = diff(parsed_expression, sym_var)
            
        # Standard Calculation / Simplification (Default)
        else:
            result = simplify(parsed_expression)

        # Return the result as a string
        return {"result": str(result)}

    except Exception as e:
        # Return a generic error message
        return {"result": f"Error: {e}"}
