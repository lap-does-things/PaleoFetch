import platform as pt
import psutil as psu
from time import sleep
from ctypes import windll
from colorama import Fore, Back, Style, init
from os import system,name
import cpuinfo
import GPUtil
gpuspec = GPUtil.getGPUs()
init()

defaultstyle = Fore.BLUE + Style.BRIGHT + Back.BLACK
# стиль логотипа!!

windll.kernel32.SetConsoleTitleW("PaleoFetch") ## Ставим название консоли
#Объявляем лого для графика
logo = {
    'Windows': r"""
                            .oodMMMM
                   .oodMMMMMMMMMMMMM
       ..oodMMM  MMMMMMMMMMMMMMMMMMM
 oodMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM
 MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM
 MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM
 MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM
 MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM
 MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM
 
 MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM
 MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM
 MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM
 MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM
 MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM
 `^^^^^^MMMMMMM  MMMMMMMMMMMMMMMMMMM
       ````^^^^  ^^MMMMMMMMMMMMMMMMM
                      ````^^^^^^MMMM
    """,
    '': r"""
                ▂▃▄▅▆▇███▀▀▀
          ▁▄▆██████▀▀
       ▗▇█████▀▀
      ▄██████▀                         ▗▇▖
    ▄█████████▅▄▂                   ▁▃▆███▙
   ▇██████████▀▀██▆▄▂▁         ▁▂▃▅█████████▖
  ▟███████████   ▔▀████▇▆▆▆▆▇▇███████████████▖
 ▟███████████▛      ▔█████████████████████████
▕████████████       ▕█████████████████████████▌
▐███████████▌       ▝▔▔▔     ▔▔▀▀▜█████████████
▐███████████                       ▀███████████▎
▕██████████▍    ▁▂▃▄▄▄▃▁            ▝██████████▎
 ██████████▙▅▆▇██████████▅▖          ▐█████████
 ▐█████████████████████████           ████████▘
  ▜███████████████████████▛          ▟███████▘
   ▜█████████████████████▛          ▗███████▘
    ▜██████████████████▀▀          ▄███████▘
     ▀████▀▀▀▀▀▀▀▀▀▀▀            ▄███████▀
       ▀█▘                    ▂▄▇██████▀
                        ▁▂▃▄▆██████▀▀
                ▄▄▄▄▄▅▅████████▀▀
                    ▔▔▔▔▔▔▔
    """,
    'Linux': r"""
         $$$$$$$        
        $$$$$$$$$       
        $$$$$$$$$$      
       $$   $   $$      
       $$/o$o\$$$$      
        $////$$$$$$     
        <<<<<$$$$$$     
        $......$$$$$    
       $........$$$$$$  
       $.........$$$$$$ 
       $.........$$$$$$$
      $..........$$$$$$$
     $$..........$$$$$$$
     $$$........$$$$$$$$
   $$$$$.......$$$$$$$$$
 $$$$$$$......$$$$$$$$$$
 $$$$$$......$$$$$$$$$$ 
   $$$        $$$$$$$$  
    """
}

#Получаем инфу о системе
#Если ты это читаешь, лпе тебя ебал кста)

sys = pt.system() # Linux, Windows, Java, etc
arch = pt.architecture()[0] # x64\x86
cpu = pt.processor() # истинное имя проца
cores, threads = psu.cpu_count(logical=False), psu.cpu_count(logical=True) # Ядра и потоки
ram = psu.virtual_memory().total // (1024 ** 3) # RANDOM ACCESS MEMORIES REFERENCE!>>!>!>!>
imf = pt.uname()
svmem = psu.virtual_memory()
swap = psu.swap_memory()
print(imf)
sleep(0.2)
#sys = "Linux" - - Дебаг


# Строим ультимативную строку Секса!!!!
sex = defaultstyle+logo.get(sys).splitlines()[0] + Fore.WHITE+" Welcome to PaleoFetch!! Like NeoFetch, but like... ancient idk"+ "\n"
sex += defaultstyle+logo.get(sys).splitlines()[1] + Fore.CYAN+"     System: " + Fore.WHITE + pt.system() +" "+ pt.release() +" "+ pt.win32_edition()+ "\n"
sex += defaultstyle+logo.get(sys).splitlines()[2] + Fore.CYAN+"     Architecture: " + Fore.WHITE +pt.machine()+"\n"
sex += defaultstyle+logo.get(sys).splitlines()[3] + Fore.CYAN+"     Kernel Ver.: " + Fore.WHITE +pt.version()+"\n"
sex += defaultstyle+logo.get(sys).splitlines()[4] + Fore.CYAN+"     CPU Name: " + Fore.WHITE  +cpuinfo.cpu.info[0]['ProcessorNameString']+"\n"
sex += defaultstyle+logo.get(sys).splitlines()[5] + Fore.CYAN+"     True CPU Name: " + Fore.WHITE +pt.processor()+"\n"
sex += defaultstyle+logo.get(sys).splitlines()[6] + Fore.CYAN+"     Cores\Threads: " + Fore.WHITE +str(cores) + Fore.CYAN+ r" \\ " + Fore.WHITE + str(threads) + Fore.CYAN +Style.DIM+ " @ "+ str(psu.cpu_freq(percpu=False)[0]) + " Ghz" + Style.NORMAL +"\n"
sex += defaultstyle+logo.get(sys).splitlines()[7] + Fore.CYAN+"     GPU Name: " + Fore.WHITE +gpuspec[0].name+ Fore.CYAN+ Style.DIM+" @ " + str(gpuspec[0].temperature)+ " °C"+ Style.NORMAL+"\n"
sex += defaultstyle+logo.get(sys).splitlines()[8] + Fore.CYAN+"     GPU Memory: " + Fore.WHITE + str(gpuspec[0].memoryTotal // 1000) + " GB"+"\n"
sex += defaultstyle+logo.get(sys).splitlines()[9] + Fore.CYAN+"     RAM: " + Fore.WHITE +str(svmem.total//1024//1024//1000) + " GB"+ Fore.CYAN+ r" \\ " + Fore.WHITE + str(svmem.total)+" Bytes"+"\n"
sex += defaultstyle+logo.get(sys).splitlines()[10] +"\n"
sex += defaultstyle+logo.get(sys).splitlines()[11] + Fore.CYAN+"     SWAP: " + Fore.WHITE +str(swap.total//1024//1024//1000) + " GB" + Fore.CYAN+ r" \\ " + Fore.WHITE + str(swap.total)+" Bytes"+"\n"
sex += defaultstyle+logo.get(sys).splitlines()[12] + "\n"
sex += defaultstyle+logo.get(sys).splitlines()[13]+"     " + Back.RED + "     "+ Back.BLUE + "     " + Back.GREEN + "     "+ Back.YELLOW + "     "+ Back.WHITE + "     "+ Back.MAGENTA + "     "+ Back.BLACK + "     "+ defaultstyle + "\n"
sex += defaultstyle+logo.get(sys).splitlines()[14]+"     " + Back.LIGHTRED_EX + "     "+ Back.LIGHTBLUE_EX + "     " + Back.LIGHTGREEN_EX + "     "+ Back.LIGHTYELLOW_EX + "     "+ Back.LIGHTWHITE_EX + "     "+ Back.LIGHTMAGENTA_EX + "     "+ Back.LIGHTBLACK_EX + "     "+ defaultstyle + "\n"
sex += defaultstyle+logo.get(sys).splitlines()[15] + "\n"
sex += defaultstyle+logo.get(sys).splitlines()[16] + "\n"
sex += defaultstyle+logo.get(sys).splitlines()[17] + Fore.CYAN+"     User: " + Fore.GREEN +pt.node()+ " aka " + psu.users()[0][0]+"\n"

# Красивый принт потому что хочу =)

system('cls' if name == 'nt' else 'clear')

for i in sex:
    print(i, flush=True,end='')
    sleep(0.001)
#print()