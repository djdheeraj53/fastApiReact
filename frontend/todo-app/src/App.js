import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
    const [todos, setTodos] = useState([]);
    const [title, setTitle] = useState('');
    const [description, setDescription] = useState('');

    useEffect(() => {
        fetchTodos();
    }, []);

    const fetchTodos = async () => {
        const response = await axios.get('http://localhost:8000/todos/');
        setTodos(response.data);
    };

    const addTodo = async () => {
        const newTodo = { title, description };
        await axios.post('http://localhost:8000/todos/', newTodo);
        fetchTodos();
        setTitle('');
        setDescription('');
    };

    const deleteTodo = async (id) => {
        await axios.delete(`http://localhost:8000/todos/${id}`);
        fetchTodos();
    };

    return (
        <div className="App">
            <h1>Todo App</h1>
            <input
                type="text"
                placeholder="Title"
                value={title}
                onChange={(e) => setTitle(e.target.value)}
            />
            <input
                type="text"
                placeholder="Description"
                value={description}
                onChange={(e) => setDescription(e.target.value)}
            />
            <button onClick={addTodo}>Add Todo</button>
            <ul>
                {todos.map((todo) => (
                    <li key={todo.id}>
                        <strong>{todo.title}</strong>: {todo.description}
                        <button onClick={() => deleteTodo(todo.id)}>Delete</button>
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default App;
