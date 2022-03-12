import React, { useState, useEffect, Fragment } from 'react';

const Dashboard = () => {
  const [userEmail, setUserEmail] = useState('');
  const [userName, setUserName] = useState('');
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (localStorage.getItem('token') === null) {
      window.location.replace('http://localhost:3000/login');
    } else {
      fetch('http://127.0.0.1:8000/contas/clientes/cond/list/', {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Token ${localStorage.getItem('token')}`
        }
      })
        .then(res => res.json())
        .then(data => {
          if(data.response){
            window.location.replace('http://localhost:3000/cliente')
          }
          else{
            alert(data.length);
              if(data.length==0){
                // escrever o formulário do condomínio
                alert("Você ainda não tem nenhum condomínio registrado.");
                window.location.replace('http://localhost:3000/tarifas');
              }
              else{
                setUserEmail(data[0].email);
                setUserName(data[0].name);
                setLoading(false);
              }
            
            }
        });
    }
  }, []);

  return (
    <div>
      <h1>Teste</h1>
      {loading === false && (
        <Fragment>
          <h1>Dashboard</h1>
          <h2>Hello {userEmail}!</h2>
          <h3>Seu nome é {userName}</h3>
        </Fragment>
      )}
    </div>
  );
};

export default Dashboard;