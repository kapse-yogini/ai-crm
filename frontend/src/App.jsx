import { useEffect, useState } from "react";

function App() {
  const [customers, setCustomers] = useState([]);
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");

  useEffect(() => {
    fetch("http://127.0.0.1:8000/customers")
      .then((res) => res.json())
      .then((data) => {
        setCustomers(data);
      });
  }, []);

  const addCustomer = async () => {
    const newCustomer = {
      name,
      email,
    };

    await fetch("http://127.0.0.1:8000/customers", {
      method: "POST",

      headers: {
        "Content-Type": "application/json",
      },

      body: JSON.stringify(newCustomer),
    });

    const response = await fetch(
      "http://127.0.0.1:8000/customers"
    );

    const updatedCustomers = await response.json();

    setCustomers(updatedCustomers);

    setName("");
    setEmail("");
  };

  const deleteCustomer = async (id) => {
    await fetch(`http://127.0.0.1:8000/customers/${id}`, {
      method: "DELETE",
    });

    const updatedCustomers = customers.filter(
      (customer) => customer.id !== id
    );

    setCustomers(updatedCustomers);
  };

  const updateCustomer = async (id) => {
    const updatedName = prompt("Enter new name");

    const updatedEmail = prompt("Enter new email");

    await fetch(`http://127.0.0.1:8000/customers/${id}`, {
      method: "PUT",

      headers: {
        "Content-Type": "application/json",
      },

      body: JSON.stringify({
        name: updatedName,
        email: updatedEmail,
      }),
    });

    const updatedCustomers = customers.map((customer) => {
      if (customer.id === id) {
        return {
          ...customer,
          name: updatedName,
          email: updatedEmail,
        };
      }

      return customer;
    });

    setCustomers(updatedCustomers);
  };

  return (
    <div style={{ padding: "20px", fontFamily: "Arial" }}>
      <h1>AI CRM</h1>

      <input
        type="text"
        placeholder="Enter name"
        value={name}
        onChange={(e) => setName(e.target.value)}
        style={{
          marginRight: "10px",
          padding: "5px",
        }}
      />

      <input
        type="email"
        placeholder="Enter email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        style={{
          marginRight: "10px",
          padding: "5px",
        }}
      />

      <button
        onClick={addCustomer}
        style={{
          padding: "5px 10px",
        }}
      >
        Add Customer
      </button>

      <hr />

      {customers.map((customer) => (
        <div
          key={customer.id}
          style={{
            border: "1px solid gray",
            padding: "10px",
            marginBottom: "10px",
            borderRadius: "5px",
          }}
        >
          <h3>{customer.name}</h3>

          <p>{customer.email}</p>

          <button
            onClick={() => deleteCustomer(customer.id)}
            style={{
              marginRight: "10px",
              padding: "5px 10px",
            }}
          >
            Delete
          </button>

          <button
            onClick={() => updateCustomer(customer.id)}
            style={{
              padding: "5px 10px",
            }}
          >
            Update
          </button>
        </div>
      ))}
    </div>
  );
}

export default App;