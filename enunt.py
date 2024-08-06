# Sistem de Management al Companiei
#
# Descriere
# Creează un sistem de management al unei companii care să permită gestionarea proiectelor,
# angajaților, echipelor, resurselor și finanțelor. Sistemul va include funcționalități pentru adăugarea
# și ștergerea proiectelor, sarcinilor, echipelor și resurselor, alocarea angajaților și resurselor către proiecte
# și urmărirea progresului și bugetelor proiectelor. Sistemul trebuie să utilizeze concepte de programare orientată
# pe obiecte (OOP), programare funcțională, decoratori și tratarea excepțiilor.
#
# Cerințe
# Structura:
#
# Definește clasele Company, Department, Project, Task, Team, Resource, Employee, Budget și Finance.
# Company va avea atribute precum nume, lista de departamente, lista de angajați și lista de resurse.
# Department va avea atribute precum nume, lista de echipe și proiecte.
# Project va avea atribute precum nume, descriere, dată de început, dată de sfârșit, buget și o listă de sarcini.
# Task va avea atribute precum titlu, descriere, termen limită, responsabil și status.
# Team va avea atribute precum nume, listă de angajați și proiecte alocate.
# Resource va avea atribute precum nume, tip, disponibilitate și cost.
# Employee va avea atribute precum nume, ID, rol, echipă și salariu.
# Budget va gestiona bugetele proiectelor și ale departamentelor.
# Finance va gestiona veniturile și cheltuielile companiei.
# Funcționalități de bază:

# Adăugarea, ștergerea și actualizarea proiectelor și sarcinilor.
# Adăugarea, ștergerea și actualizarea echipelor și angajaților.
# Alocarea angajaților și resurselor către proiecte și sarcini.
# Urmărirea progresului și bugetului proiectelor.
# Generarea rapoartelor de stare și financiare.
# Programare Funcțională:
#
# Utilizează funcții lambda și funcții de ordine superioară pentru a căuta și filtra proiectele,
# sarcinile, resursele și angajații.
# Utilizarea funcțiilor map, filter și reduce pentru diverse operațiuni în cadrul sistemului.
# Decoratori:
#
# Creează un decorator pentru logarea apelurilor funcțiilor din sistem, inclusiv timpul de
# execuție și parametrii folosiți.
# Creează un decorator pentru verificarea permisiunilor utilizatorilor înainte de a accesa
# anumite funcționalități.
# Tratarea excepțiilor:
#
# Gestionează excepțiile care pot apărea în timpul adăugării, ștergerii și actualizării proiectelor,
# sarcinilor, echipelor, angajaților și resurselor.
# Creează excepții personalizate pentru erori specifice, cum ar fi ProjectNotFoundException,
# TaskNotFoundException, ResourceUnavailableException, EmployeeNotFoundException și PermissionDeniedException.
#
# Punct bonus: Realizare meniu interactiv

# MENIU INTERACTIV
