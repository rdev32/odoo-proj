# Odoo
## Requerimientos
- _WSL_
- _Docker Desktop_
- _Python 3.10_
## Instalacion
Clone el directorio o descarguelo como zip desde la pagina web
```bash
git clone https://github.com/rdev32/odoo-proj.git
```
Utilize la linea de comandos para navegar al directorio clonado y ejecute el comando
```bash
docker compose up -d
```
Esto creara un contenedor con Oodo y PostgreSQL montando los volumenes para cargar la configuracion y los modulos nuevos.
## Monorepo
`docker run --name database -e POSTGRES_USER=odoo -e POSTGRES_PASSWORD=odoo -p 5432:5432 -d postgres:15`
## Presentacion
![Animation](https://github.com/rdev32/odoo-proj/assets/78289548/8c6881fa-fe3a-4135-837a-39d529657bc8)
