import React from "react";
import { Card, CardContent } from "@/components/ui/card";
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  PieChart,
  Pie,
  Cell,
  ResponsiveContainer
} from "recharts";

const borrowData = [
  { date: "2025-06-10", borrows: 5 },
  { date: "2025-06-11", borrows: 8 },
  { date: "2025-06-12", borrows: 3 },
  { date: "2025-06-13", borrows: 10 },
  { date: "2025-06-14", borrows: 7 },
];

const availabilityData = [
  { name: "Disponible", value: 120 },
  { name: "Emprunté", value: 30 },
];

const COLORS = ["#10B981", "#EF4444"];

const Dashboard = () => {
  return (
    <div className="grid grid-cols-1 md:grid-cols-2 gap-6 p-6">
      <Card className="shadow-lg rounded-2xl">
        <CardContent className="p-4">
          <h2 className="text-2xl font-bold mb-4">Emprunts quotidiens</h2>
          <ResponsiveContainer width="100%" height={300}>
            <BarChart data={borrowData}>
              <XAxis dataKey="date" />
              <YAxis />
              <Tooltip />
              <Bar dataKey="borrows" fill="#3B82F6" radius={[4, 4, 0, 0]} />
            </BarChart>
          </ResponsiveContainer>
        </CardContent>
      </Card>

      <Card className="shadow-lg rounded-2xl">
        <CardContent className="p-4">
          <h2 className="text-2xl font-bold mb-4">Disponibilité des livres</h2>
          <ResponsiveContainer width="100%" height={300}>
            <PieChart>
              <Pie
                data={availabilityData}
                dataKey="value"
                nameKey="name"
                cx="50%"
                cy="50%"
                outerRadius={100}
                label
              >
                {availabilityData.map((entry, index) => (
                  <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                ))}
              </Pie>
              <Tooltip />
            </PieChart>
          </ResponsiveContainer>
        </CardContent>
      </Card>
    </div>
  );
};

export default Dashboard;
