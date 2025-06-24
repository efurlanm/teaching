import subprocess
import os
from IPython.core.magic import register_cell_magic

@register_cell_magic
def c(line, cell):
    """
    Diretiva mágica para compilação e execução de código C.
    O argumento 'line' envia dados para o stdin (ex: %%c 10.5).
    """
    source_filename = 'main.c'
    executable_filename = 'main.out'
    executable_path = f'./{executable_filename}' if os.name != 'nt' else executable_filename

    try:
        with open(source_filename, 'w') as f:
            f.write(cell)

        compile_process = subprocess.run(
            ['gcc', source_filename, '-o', executable_filename],
            capture_output=True,
            text=True
        )

        if compile_process.returncode != 0:
            print("Erro de Compilação:")
            print(compile_process.stderr)
            return

        run_process = subprocess.run(
            [executable_path],
            input=line, 
            capture_output=True,
            text=True
        )
        
        if run_process.stdout:
            print(run_process.stdout)

        if run_process.stderr:
            print("Erro de Execução (stderr):", run_process.stderr)

    finally:
        for arquivo in [source_filename, executable_filename]:
            if os.path.exists(arquivo):
                os.remove(arquivo)

# Esta função é necessária para que o Jupyter reconheça o módulo como uma extensão
def load_ipython_extension(ipython):
    ipython.register_magic_function(c, 'cell')
