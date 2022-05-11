## Atividade – Python, CRON e DHCP 
O objetivo desta atividade é desenvolver um shell script bash que seja capaz de criar um arquivo de  configuração válido do servidor DHCP do GNU/Linux Debian.

A opção é fazer com que rode o script base do dhcp atualizado toda vez que a máquina desligar, mas sem  solicitar atualização ao administrador, ou seja, criar dois scripts Shell um para inicializar junto com o sistema  com as informações atualizadas e outro para rodar quando o administrador quiser fazer uma atualização. Além disso o script deve ler um arquivo de texto que contenha as informações dos computadores da rede  sendo um computador por linha. Cada linha deve conter, utilizando vírgula como separador:  
- Nome do computador
- Endereço MAC do computado
- Endereço IP do computador
  
Abaixo segue um exemplo de um arquivo de texto a ser utilizado: 
- Diretoria,00:05:84:AB:EE:FF,192.168.0.1  
- Secretaria,00:05:84:EE:2B:45,192.168.0.2  
- Tesouraria,00:05:84:4E:CB:47,192.168.0.3  
- Producao,00:05:84:2B:2A:A4,192.168.0.4
- Guarita,00:05:84:EF:12:20,192.168.0.49

Além dessa opção o script quando executado pelo administrador poderá solicitar através de menu de  escolha o que o administrador deseja fazer:
- Atualizar faixa de ip do dhcp;
- Acrescentar máquina com reserva de ip, esta opção deve atualizar o arquivo de texto também; 
- Listar as reservas já existentes;

O shell script também deve fornecer os seguintes comandos a ser acrescentado na lista acima antes de sair:  

- start: O shell script deve criar um backup do arquivo atual de configuração, criar um novo arquivo de  configuração com as informações do arquivo de texto, salvar o novo arquivo de configuração no  diretório correto e iniciar o servidor DHCP;  
- stop: O shell script deve para o servidor DHCP;  
- restart: O shell script deve chamar a função stop e start.  
- SAIR;

O script deve gerar as configurações básicas de DHCP onde a faixa de IP 192.168.0.100 e 192.168.0.149  deverá ser distribuída via DHCP e os computadores cadastrados no arquivo de texto deve-se criar as  configurações necessárias no arquivo de forma que o servidor DHCP sempre atribua o endereço IP  especificado no arquivo de texto ao computador com o endereço MAC especificado.  

Cada um dos comandos deve ser implementado utilizando funções no shell script (não existe um limite para  a quantidade de funções que deve ser criadas no shell script).

Você irá colocar opções para se o administrador deseja fazer alguma atualização no DHCP. Na outra parte da atividade você irá fazer pelo CRON, ficando a vontade quanto ao como, no caso é para  fazer o backup diário do arquivo de dhcp.conf.

Obs.: O administrador pode escolher atualizar os MACs pelo arquivo de texto, com o nome de RESERVA.txt  ou pelo script, no primeiro caso fica óbvio que ou ele roda o script para atualizar a lista no DHCP ou ele  restarta a máquina, que no caso já falamos sobre o caso de evitar está restartando o servidor em produção.
