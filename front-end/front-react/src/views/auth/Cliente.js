import React, { useState, useEffect } from 'react';

const Cliente = () => {
    const [name, setName] = useState('');
    const [phone, setPhone] = useState('');
    const [email, setEmail] = useState('');
    const [errors, setErrors] = useState(false);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        if (localStorage.getItem('token') == null) {
          window.location.replace('http://localhost:3000/login');
        } else {
          setLoading(false);
        }
      }, []);

      const onSubmit = e => {
        e.preventDefault();
    
        const user = {
          name: name,
          phone: phone,
          email: email
        };
        // alert(JSON.stringify(user));
        fetch('http://127.0.0.1:8000/contas/clientes/create/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            Authorization: `Token ${localStorage.getItem('token')}`
          },
          body: JSON.stringify(user)
        })
          .then(res => res.json())
          .then(data => {
            //alert(data.auth_token);
            window.location.replace('http://localhost:3000/dashboard');
          });
      };




    return (
    <div>
        <h2>Área do cliente</h2>
        <form onSubmit={onSubmit}>
          <label>Nome completo:</label> <br />
          <input
            name='name'
            type='text'
            value={name}
            required
            onChange={e => setName(e.target.value)}
          />{' '}
          <br />
          <label >Telefone:</label> <br />
          <input
            name='phone'
            //type='password'
            value={phone}
            required
            onChange={e => setPhone(e.target.value)}
          />{' '}
          <br />
          <label >Email:</label> <br />
          <input
            name='email'
            type='email'
            value={email}
            required
            onChange={e => setEmail(e.target.value)}
          />{' '}
          <br />
          <input type='submit' value='Salvar' />
        </form>
    </div>
    
        )
};
export default Cliente;
