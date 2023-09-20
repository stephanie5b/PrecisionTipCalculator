# PrecisionTip Calculator

# PrecisionTip Calculator: Accurate & Robust Tip Calculation

PrecisionTip Calculator is a Python-based tool developed to assist users in calculating tips with utmost accuracy and precision. Integrated with robust error handling, this tool ensures a smooth experience, regardless of the input provided.

## **Key Features**:

1. **Clear Interface** - The program provides clear prompts to users, making it easy to understand what input is required.
2. **Robust Error Handling** - Implemented with `ValueError` exception handlers, PrecisionTip guarantees uninterrupted functioning even when provided with unintended inputs.
3. **Accuracy** - Tip and total cost calculations are precise up to two decimal places.

## **Core Functions**:

### 1. `main()`

- Orchestrates the entire tipping process, guiding the user from input to output.
- Calls upon `get_cost()` and `get_tip_percent()` to retrieve necessary inputs.
- Does not execute if imported as a module in another program.

### 2. `get_cost()`

- A function dedicated to retrieving the cost of the meal.
- Ensures only valid decimal values (including integers) greater than 0 are accepted.
- Re-prompting mechanisms in place in case of erroneous inputs.

### 3. `get_tip_percent()`

- Aimed at collecting the desired tip percentage.
- Ensures only valid positive integer values are processed.
- Error handling to ensure consistent user experience.

## **Usage**:

To use the PrecisionTip Calculator, simply run the code. Follow the on-screen prompts to calculate the appropriate tip and the overall total for your meal.

