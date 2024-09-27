import { Round } from "app/app/types";
import { ItemOrderedList } from "app/components/order/ItemOrderedList";

export const RoundList = ({ rounds }: { rounds: Round[] }) => {
  if (rounds.length === 0) {
    return null;
  }

  return (
    <section>
      <h2 className="text-2xl font-semibold text-center mb-4">Order Rounds</h2>
      <ul className="space-y-4">
        {rounds.map((round, index) => (
          <li key={index} className="p-4 border border-gray-300 rounded-lg">
            <p className="font-medium">
              Round {index + 1} - Ordered at:{" "}
              {new Date(round.created).toLocaleTimeString()}
            </p>
            <ItemOrderedList items={round.items} />
          </li>
        ))}
      </ul>
    </section>
  );
};
