"""A tiny project showing how Python turns raw data into decisions."""

from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from functools import cached_property
import json
from statistics import mean, median


@dataclass(frozen=True)
class Sale:
    customer: str
    product: str
    category: str
    amount: float
    rating: int


class SalesAnalyzer:
    def __init__(self, sales: list[Sale]):
        self.sales = sales

    @cached_property
    def total_revenue(self) -> float:
        return sum(sale.amount for sale in self.sales)

    @cached_property
    def revenue_by_category(self) -> dict[str, float]:
        totals = defaultdict(float)
        for sale in self.sales:
            totals[sale.category] += sale.amount
        return dict(sorted(totals.items(), key=lambda item: item[1], reverse=True))

    @property
    def top_products(self) -> list[tuple[str, float]]:
        totals = defaultdict(float)
        for sale in self.sales:
            totals[sale.product] += sale.amount
        return sorted(totals.items(), key=lambda item: item[1], reverse=True)

    @property
    def insights(self) -> dict[str, object]:
        amounts = [sale.amount for sale in self.sales]
        ratings = [sale.rating for sale in self.sales]
        most_common_category = Counter(sale.category for sale in self.sales).most_common(1)[0]
        high_value_sales = [sale for sale in self.sales if sale.amount >= median(amounts)]

        return {
            "total_revenue": round(self.total_revenue, 2),
            "average_sale": round(mean(amounts), 2),
            "median_sale": round(median(amounts), 2),
            "average_rating": round(mean(ratings), 2),
            "leading_category": most_common_category[0],
            "high_value_orders": len(high_value_sales),
            "top_3_products": [
                {"product": product, "revenue": round(revenue, 2)}
                for product, revenue in self.top_products[:3]
            ],
            "revenue_by_category": {
                category: round(revenue, 2)
                for category, revenue in self.revenue_by_category.items()
            },
        }

    def print_dashboard(self) -> None:
        print("\n" + "=" * 58)
        print("PYTHON POWER DEMO | SALES INTELLIGENCE DASHBOARD")
        print("=" * 58)
        print(f"Orders analysed : {len(self.sales)}")
        print(f"Total revenue   : Rs. {self.total_revenue:,.2f}")
        print(f"Average rating  : {self.insights['average_rating']}/5")
        print("\nRevenue by category")
        for category, revenue in self.revenue_by_category.items():
            bar = "#" * int(revenue / 1000)
            print(f"  {category:<12} Rs. {revenue:>8,.2f}  {bar}")

        print("\nTop products")
        for position, (product, revenue) in enumerate(self.top_products[:3], start=1):
            print(f"  {position}. {product:<16} Rs. {revenue:,.2f}")

        print("\nAutomatic insight")
        print(
            f"  Focus on {self.insights['leading_category']} and promote "
            f"{self.top_products[0][0]} next month."
        )

    def export_report(self, filename: str = "sales_report.json") -> None:
        report = {"summary": self.insights, "orders": [asdict(sale) for sale in self.sales]}
        with open(filename, "w", encoding="utf-8") as report_file:
            json.dump(report, report_file, indent=2)
        print(f"\nJSON report saved to {filename}")


def main() -> None:
    sales = [
        Sale("Aisha", "Laptop", "Electronics", 78000, 5),
        Sale("Bilal", "Headphones", "Electronics", 8500, 4),
        Sale("Sara", "Python Book", "Books", 1800, 5),
        Sale("Hamza", "Office Chair", "Furniture", 12500, 4),
        Sale("Noor", "Laptop", "Electronics", 82000, 5),
        Sale("Ali", "Python Book", "Books", 2200, 4),
        Sale("Hina", "Desk Lamp", "Furniture", 3200, 3),
        Sale("Omar", "Headphones", "Electronics", 9200, 4),
        Sale("Zoya", "Office Chair", "Furniture", 11800, 5),
    ]

    analyzer = SalesAnalyzer(sales)
    analyzer.print_dashboard()
    analyzer.export_report()


if __name__ == "__main__":
    main()
