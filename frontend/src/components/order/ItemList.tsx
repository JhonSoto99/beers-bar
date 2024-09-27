import { Item } from "app/app/types";

export const ItemList = ({ items }: { items: Item[] }) => {
  return (
    <section className="mb-6">
      <h2 className="text-2xl font-semibold text-center text-gray-700 mb-4">
        Items Ordered
      </h2>
      <ul className="space-y-4">
        {items.map((item, index) => (
          <li key={index} className="p-4 border border-gray-300 rounded-lg">
            <p className="font-bold text-lg">{item.name}</p>
            <p className="text-gray-600">
              Price per unit: ${item.price_per_unit}
            </p>
            <p className="text-gray-600">Total: ${item.total}</p>
          </li>
        ))}
      </ul>
    </section>
  );
};
