# EgaPro Project

## Installation et exécution

### 1. Cloner le projet
```bash
git clone https://github.com/user/egapro_project.git
cd egapro_project
```

### 2. Placer le fichier CSV dans le dossier `/data`
- `index-egalite-fh-utf8.csv`

### 3. Lancer les services avec Docker
```bash
docker-compose up --build
```

### 4. Accéder aux services
- **API REST:** `http://localhost/api/v1/entreprises`
- **gRPC:** `grpcurl -plaintext localhost:50051 list`
- **Swagger:** `http://localhost/api/v1/apidocs`
```
