# GruPy Blumenau Thumbs

[![Testes unitários](https://github.com/pythonbnu/thumbs/actions/workflows/unit-tests.yaml/badge.svg)](https://github.com/pythonbnu/thumbs/actions/workflows/unit-tests.yaml)

Gerador de banners para os encontros do GruPy Blumenau.

```shell
$ pip install git+https://github.com/pythonbnu/thumbs.git@main
```

### Dependências

É necessário ter o **Chromium** ou **Google Chrome** instalado e visível no `PATH` do seu sistema para poder executar o módulo adequadamente.

- [Download Chromium](https://www.chromium.org/getting-involved/download-chromium/)

### Executando

```
$ grupy_thumbs

? Para qual meetup você deseja criar o banner? 32º encontro do Grupy Blumenau - 29/07/2023
? Template deseja usar? meetup.html
? Insira o caminho ou URL para uma imagem customizada: https://www.furb.br/web/upl/noticias/201401/escadaria_site.jpg
? Qual o horário do evento? 10:00 AM

[0706/155027.044569:WARNING:sandbox_linux.cc(393)] InitializeSandbox() called with multiple threads in process gpu-process.
[0706/155027.059686:WARNING:bluez_dbus_manager.cc(247)] Floss manager not present, cannot set Floss enable/disable.
594551 bytes written to file /home/jjpaulo2/screenshot.png
```

#### Banner gerado pelo módulo

![screenshot](https://github.com/pythonbnu/thumbs/assets/22819523/09447293-e0e7-414c-afe6-55f7c6c10b44)
