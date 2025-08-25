---
sidebar_position: 1
---

# Cómo colaborar

Comencemos.

## Para iniciar

- Crea una cuenta de [github](https://github.com/)
### Qué software necesitas

- Instala [Node.js](https://nodejs.org/en/download/) version 22 or superior:
  - Una vez que instales **Node** verifica las dependencia
- Instala un [cliente de git](https://desktop.github.com/download/)
  - Conecta tu cuenta de github
- Clona el repositorio [my-website](https://github.com/conecta-clanes/my-website)
  - Puedes seguir las instrucciones [Clonar un repositorio](https://docs.github.com/es/repositories/creating-and-managing-repositories/cloning-a-repository)
- Instala [Yarn](https://classic.yarnpkg.com/lang/en/docs/install/#windows-stable )

## Para iniciar

- Accede a la carpeta de repositorio **my-website**

```bash
cd my-website
```
- Crea un nuevo documento con extension markdown sobre la carpeta de **docs**


## Para probar localmente

Ejecuta el comando 

```bash
cd my-website
yarn clear 
yarn install
yarn add @docusaurus/theme-mermaid
yarn run start
```

- Se abre automaticamente el sitio en un navegador web
  - si no inicia automaticamente puedes acceder a **http://localhost:3000/my-website/**


## Para deployar

- Sube tus cambios al repositorio vía un cliente de git con la descripción de tu provincia en 3 letras seguidas de guión seguida de 3 digitos de tu grupo con una descripción de la aportación

```bash
AZC-000 Alguna descripción de la aportación
```


## Para agregar elementos al sitio

- En el apartado de **Docs*>Para agregar elementos al sitio** puedes ver un ficha de Markdown, como crear una página, como crear un documento, como crear un elemento del Blog, puede ver más ligas relacionadas con **Docusaurus**

#Thoublesgooting

Se puede solucionar lo problema ejecutando los comandos
```bash
npm i
npm install docusaurus
npm install mermaid
npm audit fix
npm run start
```

### Dónde puedo encontrar los icons

Existen varias páginas por ejemplo [Icons](https://gist.github.com/rxaviers/7360908)