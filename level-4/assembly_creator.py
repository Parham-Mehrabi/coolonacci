import subprocess


while True:
    try:
        maximum = int(input('set a maximum for the sequence: '))
        break
    except ValueError:
        print('the input must be a number')


assembly_code = f"""

section .data
    space db ' '
    endline db 10

section .text
    global _start


_start:
    mov rax, 1
    mov rbx, 1
    mov r8, 0

addition:
    inc r8
    call print_number

    mov rdx, rbx
    add rbx, rax
    mov rax, rdx

    push rax
    mov rsi, space
    mov rax, 1
    mov rdi, 1
    mov rdx, 1
    syscall
    pop rax

    cmp rax, {maximum}
    jl addition

print_end_line:
    mov rsi, endline
    mov rax, 1
    mov rdi, 1
    mov rdx, 1
    syscall

exit_program:
    mov rax, 60
    xor rdi, rdi
    syscall

print_number:
    push r12
    push rax
    mov r12, rax
    mov rcx, 10
    xor r9, r9
    

extraction:
    mov rax, r12
    xor rdx, rdx
    div rcx
    mov r12, rax

    add rdx, 48
    push rdx
    inc r9

    cmp r12, 0
    jne extraction


print_loop:

    mov rax, 1
    mov rdi, 1
    mov rsi, rsp
    mov rdx, 1
    syscall

    pop rax
    dec r9
    cmp r9, 0
    jg print_loop
    
    ;mov rax, r12

    pop rax
    pop r12

    ret

"""

with open('./level-4/fibo.asm', 'w+') as f:
    f.write(assembly_code)



subprocess.run(
    ['nasm', '-f', 'elf64', './level-4/fibo.asm', '-o', './level-4/fibo.o'],
    check=True
)

subprocess.run(
    ['ld', './level-4/fibo.o', '-o', './level-4/fibo'],
    check=True
)

subprocess.run(
    ['./level-4/fibo'],
    check=True
)
