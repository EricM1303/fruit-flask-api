<h1 style="display: inline-flex; align-items: center;">Fruit Flask API <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExenZxdmhmbGx3YXd4eDZkb2J2ejU3a3B0czBieHluY2d5bHI0NzkwbyZlcD12MV9zdGlja2Vyc19zZWFyY2gmY3Q9cw/EcgMJvuEGKsLQAJVqs/giphy.gif" alt="Frutas dançantes" style="width:90px; height:auto; margin-left:10px;"></h1> 

Uma API simples para gerenciar frutas. Ela permite listar todas as frutas, adicionar novas frutas, listar uma fruta específica por ID e excluir frutas, seja por ID ou todas de uma vez. Ideal para demonstrar operações básicas de CRUD via Postman (Create, Read, Update, Delete).  

***  

## ⚙️ Funcionalidades  
Através de requisições via Postman, você pode realizar tarefas como:  
- 👀 Visualizar a lista de frutas disponíveis na API (por ID ou todas de uma vez)  
- ✍️ Alterar informações de uma fruta  
- 🗑️ Excluir frutas pelo ID

Para realizar essas operações, siga o passo a passo abaixo.  

***  

## 📋 Requisitos  
* 🛠️ Postman instalado na máquina ou outra IDE para requisições  
* 🌐 Porta 3000 liberada no localhost (máquina atual)  

***  

## 🚀 Como utilizar a API  

### 👀 Visualizar lista de frutas:  
* Inserir o endereço ```localhost:3000/frutas``` (Utilizar o método *GET request*).  

### 🔍 Visualizar uma fruta através do ID:  
* IDs disponíveis inicialmente: 1 a 4 (antes de adicionar novas frutas).  
* Inserir o endereço ```localhost:3000/frutas/id``` (Utilizar o método *GET request*).  

### ➕ Adicionar frutas à lista:  
* Enviar requisição em formato *JSON*.  
* Campos necessários: Id, Nome da fruta, Cor da fruta, Quantidade.  
* Inserir o endereço ```localhost:3000/frutas``` e usar o método *POST*.  

### ✍️ Alterar alguma fruta da lista:  
* Alterar dados em formato *JSON*.  
* Utilizar o endereço ```localhost:3000/frutas``` com o método *PUT*.  

### 🗑️ Deletar frutas:  
* Para deletar uma fruta específica: ```localhost:3000/frutas/id``` com o método *DELETE*.  
 
***  

### 👨‍💻 Autor do projeto  

* Eric Matheus N Campelo  
 

