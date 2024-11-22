Franck-Hertz Experiment

Este repositório contém scripts e dados relacionados à análise do experimento de Franck-Hertz. O experimento é uma das primeiras confirmações experimentais da teoria quântica, demonstrando a quantização da energia em átomos.
📖 Contexto Teórico

O experimento de Franck-Hertz, realizado em 1914 por James Franck e Gustav Hertz, é uma comprovação fundamental da teoria quântica. Ele mostra que os elétrons interagem com átomos apenas em níveis discretos de energia, evidenciando os estados excitados dos átomos.

    Princípio: Um feixe de elétrons colide com átomos de mercúrio (ou outro gás), transferindo energia. Os elétrons perdem energia em quantidades específicas correspondentes às transições entre níveis energéticos dos átomos.
    Resultados: Ao variar a tensão e temperatura aplicada, a corrente medida exibe picos e vales que correspondem às energias de excitação dos átomos.

⚙️ Descrição Técnica

Este repositório contém:

    Scripts Python para processar os dados do experimento.
    Dados experimentais em arquivos .csv.
    Resultados processados, como gráficos e arquivos contendo picos e médias de distâncias.

🛠️ Configuração e Execução
1. Pré-requisitos

Certifique-se de ter instalado:

    Python 3.7 ou superior.
    As bibliotecas:
        pandas
        numpy
        matplotlib
        scipy

Você pode instalá-las com:

pip install pandas numpy matplotlib scipy

2. Como Executar

    Coloque os arquivos .csv dos dados experimentais na pasta data/.

    Execute o script principal:

    python scripts/process_franck_hertz.py

    Os resultados serão gerados em:
        results/: Contendo gráficos (.png) e arquivos de resultados (.csv).

📊 Exemplo de Resultados
Gráfico Ajustado com Spline Cúbica

Arquivo de Resultados
Pico (Tensão - Dados)	Pico (Corrente - Dados)	Média Distância Picos - Dados (V)	Pico (Tensão - Ajuste)	Pico (Corrente - Ajuste)	Média Distância Picos - Ajuste (V)
1.23	2.45	1.52	1.25	2.50	1.48
2.75	3.56		2.70	3.60	
4.30	4.89		4.20	4.95	
🔬 Principais Funcionalidades

    Ajuste por Spline Cúbica:
        Gera uma curva suave com base nos dados experimentais.
        Utiliza a biblioteca scipy.interpolate para ajuste preciso.

    Detecção de Picos:
        Usa scipy.signal.find_peaks para identificar os picos de corrente nos dados experimentais e na curva ajustada.

    Cálculo de Médias de Distâncias:
        Calcula a média das distâncias entre picos consecutivos, evidenciando as transições energéticas.

    Visualização e Exportação:
        Salva gráficos dos ajustes e resultados detalhados em arquivos .csv.

🧪 Aplicações

Este repositório pode ser usado para:

    Ensino: Demonstrar a análise de dados experimentais no contexto de física.
    Pesquisa: Processar e interpretar dados experimentais de forma automatizada.
📜 Referências
    https://edisciplinas.usp.br/pluginfile.php/6619417/mod_resource/content/2/ep2_2021.pdf
    https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.find_peaks.html
