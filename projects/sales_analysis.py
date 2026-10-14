"""Summarize a sample sales dataset and export a JSON report."""

from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
import json
from pathlib import Path
from statistics import mean, median


@dataclass(frozen=True)
class Sale:
    customer: str
    product: str
    category: str
    amount: float
    rating: int


class SalesAnalyzer:
    def __init__(self, sales: list[Sale]) -> None:
        if not sales:
            raise ValueError("sales must contain at least one order")
        self.sales = sales

    @property
    def total_revenue(self) -> float:
        return sum(sale.amount for sale in self.sales)

    @property
    def revenue_by_category(self) -> dict[str, float]:
        totals: defaultdict[str, float] = defaultdict(float)
        for sale in self.sales:
            totals[sale.category] += sale.amount
        return dict(sorted(totals.items(), key=lambda item: item[1], reverse=True))

    @property
    def top_products(self) -> list[tuple[str, float]]:
        totals: defaultdict[str, float] = defaultdict(float)
        for sale in self.sales:
            totals[sale.product] += sale.amount
        return sorted(totals.items(), key=lambda item: item[1], reverse=True)

    @property
    def insights(self) -> dict[str, object]:
        amounts = [sale.amount for sale in self.sales]
        ratings = [sale.rating for sale in self.sales]
        leading_category = Counter(sale.category for sale in self.sales).most_common(1)[0][0]
        return {
            "total_revenue": round(self.total_revenue, 2),
            "average_sale": round(mean(amounts), 2),
            "median_sale": round(median(amounts), 2),
            "average_rating": round(mean(ratings), 2),
            "leading_category": leading_category,
            "high_value_orders": sum(amount >= median(amounts) for amount in amounts),
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
        print("Sales analysis")
        print(f"Orders: {len(self.sales)}")
        print(f"Total revenue: Rs. {self.total_revenue:,.2f}")
        print(f"Average rating: {self.insights['average_rating']}/5")
        print("Revenue by category:")
        largest_revenue = max(self.revenue_by_category.values())
        for category, revenue in self.revenue_by_category.items():
            bar = "#" * max(1, round(revenue / largest_revenue * 30))
            print(f"  {category:<12} Rs. {revenue:>8,.2f}  {bar}")
        print("Top products:")
        for position, (product, revenue) in enumerate(self.top_products[:3], start=1):
            print(f"  {position}. {product:<16} Rs. {revenue:,.2f}")

    def export_report(self, filename: Path | None = None) -> Path:
        output_path = filename or Path("data/output/sales_report.json")
        output_path.parent.mkdir(parents=True, exist_ok=True)
        report = {"summary": self.insights, "orders": [asdict(sale) for sale in self.sales]}
        output_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
        return output_path


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
    print("Report:", analyzer.export_report())


if __name__ == "__main__":
    main()