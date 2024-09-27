import { render, screen } from "@testing-library/react";
import { ItemList } from "../components/order/ItemList";
import { Item } from "app/app/types";

describe("ItemList Component", () => {
  it("renders items correctly", () => {
    const items: Item[] = [
      { name: "Item 1", price_per_unit: 10, total: 30 },
      { name: "Item 2", price_per_unit: 15, total: 45 },
    ];

    render(<ItemList items={items} />);

    expect(screen.getByText("Items Ordered")).toBeInTheDocument();
    expect(screen.getByText("Item 1")).toBeInTheDocument();
    expect(screen.getByText("Item 2")).toBeInTheDocument();

    expect(screen.getByText("Price per unit: $10")).toBeInTheDocument();
    expect(screen.getByText("Total: $30")).toBeInTheDocument();
    expect(screen.getByText("Price per unit: $15")).toBeInTheDocument();
    expect(screen.getByText("Total: $45")).toBeInTheDocument();
  });

  it("renders nothing if items array is empty", () => {
    render(<ItemList items={[]} />);

    expect(screen.getByText("Items Ordered")).toBeInTheDocument();
    expect(screen.queryByText("Item 1")).not.toBeInTheDocument();
    expect(screen.queryByText("Item 2")).not.toBeInTheDocument();
  });
});
