"""A scientific calculator that evaluates a restricted set of expressions."""

import ast
import math
from collections.abc import Callable


class ScientificCalculator:
    FUNCTIONS: dict[str, Callable[..., float]] = {
        name: getattr(math, name)
        for name in (
            "acos", "asin", "atan", "ceil", "cos", "degrees", "exp",
            "floor", "log", "log10", "radians", "sin", "sqrt", "tan",
        )
    }
    FUNCTIONS["abs"] = abs
    FUNCTIONS["factorial"] = math.factorial
    CONSTANTS = {"e": math.e, "pi": math.pi, "tau": math.tau}

    def calculate(self, expression: str) -> float | int:
        try:
            tree = ast.parse(expression, mode="eval")
            result = self._evaluate(tree.body)
        except (SyntaxError, ValueError, TypeError, ZeroDivisionError, OverflowError) as error:
            raise ValueError(f"Invalid expression: {error}") from error

        if isinstance(result, float) and result.is_integer():
            return int(result)
        return result

    def _evaluate(self, node: ast.AST) -> float | int:
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            return node.value
        if isinstance(node, ast.Name) and node.id in self.CONSTANTS:
            return self.CONSTANTS[node.id]
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
            value = self._evaluate(node.operand)
            return value if isinstance(node.op, ast.UAdd) else -value
        if isinstance(node, ast.BinOp) and type(node.op) in {
            ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Pow, ast.Mod, ast.FloorDiv,
        }:
            left = self._evaluate(node.left)
            right = self._evaluate(node.right)
            operations = {
                ast.Add: lambda: left + right,
                ast.Sub: lambda: left - right,
                ast.Mult: lambda: left * right,
                ast.Div: lambda: left / right,
                ast.Pow: lambda: left ** right,
                ast.Mod: lambda: left % right,
                ast.FloorDiv: lambda: left // right,
            }
            return operations[type(node.op)]()
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            if node.func.id not in self.FUNCTIONS or node.keywords:
                raise ValueError("Function is not supported")
            arguments = [self._evaluate(argument) for argument in node.args]
            return self.FUNCTIONS[node.func.id](*arguments)
        raise ValueError("Only numbers, operators, constants, and supported functions are allowed")

    def run(self) -> None:
        print("Scientific calculator. Type 'help' or 'quit'.")
        while True:
            try:
                expression = input("calc> ").strip()
            except EOFError:
                break
            if expression.lower() in {"quit", "exit", "q"}:
                break
            if expression.lower() == "help":
                print("Functions:", ", ".join(sorted(self.FUNCTIONS)))
                print("Constants: e, pi, tau | Operators: + - * / // % **")
                continue
            if expression:
                try:
                    print("=", self.calculate(expression))
                except ValueError as error:
                    print("Error:", error)


if __name__ == "__main__":
    ScientificCalculator().run()