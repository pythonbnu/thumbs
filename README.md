# GruPy Blumenau Thumbs

[![Testes unitários](https://github.com/pythonbnu/thumbs/actions/workflows/unit-tests.yaml/badge.svg)](https://github.com/pythonbnu/thumbs/actions/workflows/unit-tests.yaml)

Gerador de banners para os encontros do GruPy Blumenau.

```shell
$ pip install git+https://github.com/pythonbnu/thumbs.git@main
```

### Dependências

É necessário ter o **Chromium** ou **Google Chrome** instalados e visíveis no `PATH` do seu sistema para poder execurar o módulo adequeadamente.

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
