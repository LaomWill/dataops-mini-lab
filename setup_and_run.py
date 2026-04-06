import os
import subprocess
import time
import sys

def run_command(command, description):
    print(f"\n🚀 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ Sucesso: {description}")
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro em {description}: {e.stderr}")
        return None

def main():
    print("="*60)
    print("  AUTOMAÇÃO DATAOPS: TEMPORAL + MONGODB ATLAS + DOCKER")
    print("="*60)

    # 1. Instalar dependências
    run_command("pip install -r requirements.txt", "Instalando dependências do Python")

    # 2. Subir Docker Compose
    run_command("docker-compose up -d", "Iniciando containers do Temporal via Docker")

    print("\n⏳ Aguardando 15 segundos para o Temporal Server iniciar...")
    time.sleep(15)

    # 3. Iniciar o Worker em segundo plano
    print("\n👷 Iniciando o Worker em segundo plano...")
    # No Windows usamos 'start /B', no Linux/Mac usamos '&'
    if os.name == 'nt':
        worker_proc = subprocess.Popen("set PYTHONPATH=. && python app/worker.py", shell=True)
    else:
        worker_proc = subprocess.Popen("PYTHONPATH=. python3 app/worker.py", shell=True)
    
    time.sleep(5) # Aguarda o worker conectar

    # 4. Executar o Workflow
    print("\n🎬 Disparando o Workflow de Ingestão...")
    if os.name == 'nt':
        run_command("set PYTHONPATH=. && python app/run_workflow.py", "Executando Workflow")
    else:
        run_command("PYTHONPATH=. python3 app/run_workflow.py", "Executando Workflow")

    print("\n" + "="*60)
    print("  PROCESSO CONCLUÍDO COM SUCESSO!")
    print("  Verifique seu MongoDB Atlas e a UI do Temporal em http://localhost:8080")
    print("="*60)
    
    # Mantém o worker rodando se o usuário quiser, ou encerra
    input("\nPressione ENTER para encerrar o Worker e finalizar...")
    worker_proc.terminate()

if __name__ == "__main__":
    main()
