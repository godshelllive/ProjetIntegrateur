from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration, StudentRegistration2, StudentRegistration3, StudentRegistration4, StudentRegistration5
from .models import form_1, form_2, form_3, form_5, verification0
from django.contrib import messages
from django.shortcuts import redirect
Nombre_Heure = 0


# Create your views here.


#--------------     FONCTIONS POUR L'AJOUT ET L'AFFICHAGE DANS LA BASE DE DONNEES     -----------------


def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            nb = fm.cleaned_data['number']
            ag = fm.cleaned_data['age']
            st = fm.cleaned_data['state']

            #       Comparaison de la base de donnees avec les donnees entrees :

            filtrage_de_donnees = form_1.objects.filter(name = nm, email = em, number = nb, age = ag, state = st.upper()).exists()
            filtrage_de_donnees2 = form_1.objects.filter(state = st.upper()).exists()
            
    #    -------------------   verifications   ---------------------------
            if not filtrage_de_donnees2 and (not "DIRECTEUR" in st.upper() or not "DIRECTRICE" in st.upper()):
                if filtrage_de_donnees:
                            #   ALORS LES DONNEEES EXISTENT DEJA
                    messages.warning(request, "Nous avons un membre de la communauté qui existe déjà avec ces identifiants.")
                else:
                            #   ALORS LES DONNEEES SONT ENREGISTRER AVEC SUCCES
                    enregistre_a_nouveau = form_1(name = nm, email = em, password = pw, number = nb, age = ag, state = st.upper())
                    enregistre_a_nouveau.save()
                    messages.success(request, "ENREGISTRE AVEC SUCCES !\n\n")
                    messages.success(request, "VOUS ETES DESORMAIS MEMBRE DE LA COMMUNAUTE !\n")
                    messages.success(request, "Vous pouvez désormais vous connecter à votre compte.")
            else:
                messages.success(request, "UN SEUL DIRECTEUR EST AUTORISE DANS LA COMMUNAUTE ET IL Y EN A DEJA UN !\n\n")
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    partner = form_1.objects.all()           #       nouvel element !!
    return render(request, 'Etudiant/addandshow.html', {'form': fm, 'partner' : partner})    #  Ajout des objets creez ! 


def connect(request):
    global perm, name, state
    perm = "None"
    if request.method == 'POST':
        fm = StudentRegistration2(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            st = fm.cleaned_data['state']

            #       Comparaison de la base de donnees avec les donnees entrees :

            filtrage_de_donnees = form_1.objects.filter(name = nm, password = pw, email = em, state = st.upper()).exists()
            
    #    -------------------   verifications   ---------------------------
            if filtrage_de_donnees:
                        #   ALORS LES DONNEEES EXISTENT DEJA
                if 'MAITRESSE' in st.upper() or 'CHERCHEUR' in st.upper() or 'CHERCHEUSE' in st.upper() or 'MAITRE' in st.upper() or 'PROF' in st.upper() or 'ENSEIGNANT' in st.upper() or 'CHEF' in st.upper() or 'PROFESSEUR' in st.upper() or 'MASTER' in st.upper() or 'DOCTEUR' in st.upper():
                    messages.warning(request, "CONNECTE !")
                    perm = "MI-BOSS"
                    name = nm
                    state = st
                    partner = form_1.objects.all()           #       nouvel element !!
                    return render(request, 'Etudiant/professeur.html', {'name': name, 'state': state, 'partner': partner})
                if 'ELEVE' in st.upper() or 'ETUDIANT' in st.upper() or 'AMI' in st.upper() or 'ECOLIER' in st.upper() or 'STUDENT' in st.upper() or 'L1' in st.upper() or 'L2' in st.upper() or 'L3' in st.upper():
                    messages.warning(request, "CONNECTE !")
                    perm = "CHILD"
                    name = nm
                    state = st
                    partner = form_1.objects.all()           #       nouvel element !!
                    return render(request, 'Etudiant/client.html', {'name': name, 'state': state, 'partner': partner})
                if 'DIRECTEUR' in st.upper() or 'DIRECTRICE' in st.upper():
                    messages.warning(request, "CONNECTE !")
                    perm = "BOSS"
                    name = nm
                    state = st
                    partner = form_1.objects.all()           #       nouvel element !!
                    return render(request, 'Etudiant/directeur.html', {'name': name, 'state': state, 'partner': partner})

            else:
                messages.warning(request, "DESOLE !\nNous ne trouvons pas vos informations :(\nVous semblez ne pas être présent dans notre communauté.\n Passez vous inscrire avant de vous connecter !")
    else:
        fm = StudentRegistration2()
    return render(request, 'Etudiant/connextion.html', {'form': fm})    #  Ajout des objets creez ! 

#-------------------     FONCTION DE SUPPRESSION DES DONNEES DE LA BASE DE DONNNES      -----------------

def delete_path(request, id):
    if request.method == 'POST':
        sup = form_1.objects.get(pk = id)
        sup.delete()
        if perm == "BOSS":
            partner = form_1.objects.all()           #       nouvel element !!
            return render(request, 'Etudiant/directeur.html', {'name': name, 'state': state, 'partner': partner})
        elif perm == "MI-BOSS":
            partner = form_1.objects.all()           #       nouvel element !!
            return render(request, 'Etudiant/professeur.html', {'name': name, 'state': state, 'partner': partner})
        elif perm == "CHILD":
            partner = form_1.objects.all()           #       nouvel element !!
            return render(request, 'Etudiant/client.html', {'name': name, 'state': state, 'partner': partner})


def modifie_path(request, id):
    if request.method == 'POST':
        sup = form_1.objects.get(pk = id)
        fm = StudentRegistration(request.POST, instance = sup)
        if fm.is_valid():
            fm.save()
            if perm == "BOSS":
                partner = form_1.objects.all()           #       nouvel element !!
                return render(request, 'Etudiant/directeur.html', {'name': name, 'state': state, 'partner': partner})
            elif perm == "MI-BOSS":
                partner = form_1.objects.all()           #       nouvel element !!
                return render(request, 'Etudiant/professeur.html', {'name': name, 'state': state, 'partner': partner})
            elif perm == "CHILD":
                partner = form_1.objects.all()           #       nouvel element !!
                return render(request, 'Etudiant/client.html', {'name': name, 'state': state, 'partner': partner})
    else:
        sup = form_1.objects.get(pk = id)
        fm = StudentRegistration(instance = sup)
    return render(request, 'Etudiant/updatestudent.html', {'form': fm})

def load_bdd(request):
    partner = form_1.objects.all()
    return render(request, 'Etudiant/base_de_donnee.html' , {'partner' : partner})






def profs(request):
    partner = form_1.objects.all()
    return render(request, 'Etudiant/professeur.html' , {'partner' : partner}) 

def clients(request):
    partner = form_1.objects.all()
    return render(request, 'Etudiant/client.html' , {'partner' : partner}) 

def directeurs(request):
    partner = form_1.objects.all()
    return render(request, 'Etudiant/directeur.html' , {'partner' : partner}) 

def v_emploie(request):
    partner0 = form_5.objects.all()
    return render(request, 'Etudiant/vue_emploie.html' , {'partner0' : partner0})

def pre_rmp(request):
    global Pass, information
    Pass = ""
    information = ""
    if request.method == 'POST':
        fm = StudentRegistration3(request.POST)
        if fm.is_valid():
            jr = fm.cleaned_data['jour']
            nm = fm.cleaned_data['nom']
            st = fm.cleaned_data['sept_heure']
            ht = fm.cleaned_data['huit_heure']
            nf = fm.cleaned_data['neuf_heure']
            dx = fm.cleaned_data['dix_heure']
            oz = fm.cleaned_data['onze_heure']
            dz = fm.cleaned_data['douze_heure']
            tz = fm.cleaned_data['treize_heure']
            qaz = fm.cleaned_data['quatorze_heure']
            qiz = fm.cleaned_data['quinze_heure']
            sz = fm.cleaned_data['seize_heure']
            ds = fm.cleaned_data['dix_sept_heure']
            dht = fm.cleaned_data['dix_huit_heure']
            dnf = fm.cleaned_data['dix_neuf_heure']


            if jr.upper() != "LUNDI" and jr.upper() != "MARDI" and jr.upper() != "MERCREDI" and jr.upper() != "JEUDI" and jr.upper() != "VENDREDI" and jr.upper() != "SAMEDI":
                information = "Entrez des jours valides s'il vous plait !\n( Lundi, Mardi, Mercredi, Jeudi, Vendredi, Samedi )"
                return render(request, 'Etudiant/pre_remplissage.html', {'information': information})



            form_5_obj = form_5.objects.first()
            if jr.upper() == "LUNDI":
                if st.upper() == "OK":
                    if form_5_obj is None:
                        form_5_obj = form_5.objects.get(id = 13)
                        form_5_obj.lundi += "7 heures à 8 heures par " + nm + "\n"
                        form_5_obj.save()
                    else:
                        form_5_obj = form_5.objects.get(id = 13)
                        form_5_obj.lundi += "7 heures à 8 heures par " + nm + "\n"
                        form_5_obj.save()
                if ht.upper() == "OK":
                    if form_5_obj is None:
                        form_5_obj = form_5.objects.get(id = 12)
                        form_5_obj.lundi += "8 heures à 9 heures par " + nm + "\n"
                        form_5_obj.save()
                    else:
                        form_5_obj = form_5.objects.get(id = 12)
                        form_5_obj.lundi += "8 heures à 9 heures par " + nm + "\n"
                        form_5_obj.save()
                if nf.upper() == "OK":
                    if form_5_obj is None:
                        form_5_obj = form_5.objects.get(id = 11)
                        form_5_obj.lundi += "9 heures à 10 heures par " + nm + "\n"
                        form_5_obj.save()
                    else:
                        form_5_obj = form_5.objects.get(id = 11)
                        form_5_obj.lundi += "9 heures à 10 heures par " + nm + "\n"
                        form_5_obj.save()
                if dx.upper() == "OK":
                    if form_5_obj is None:
                        form_5_obj = form_5.objects.get(id = 10)
                        form_5_obj.lundi += "10 heures à 11 heures par " + nm + "\n"
                        form_5_obj.save()
                    else:
                        form_5_obj = form_5.objects.get(id = 10)
                        form_5_obj.lundi += "10 heures à 11 heures par " + nm + "\n"
                        form_5_obj.save()
                if oz.upper() == "OK":
                    if form_5_obj is None:
                        form_5_obj = form_5.objects.get(id = 9)
                        form_5_obj.lundi += "11 heures à 12 heures par " + nm + "\n"
                        form_5_obj.save()
                    else:
                        form_5_obj = form_5.objects.get(id = 9)
                        form_5_obj.lundi += "11 heures à 12 heures par " + nm + "\n"
                        form_5_obj.save()
                if dz.upper() == "OK":
                    if form_5_obj is None:
                        form_5_obj = form_5.objects.get(id = 8)
                        form_5_obj.lundi += "12 heures à 13 heures par " + nm + "\n"
                        form_5_obj.save()
                    else:
                        form_5_obj = form_5.objects.get(id = 8)
                        form_5_obj.lundi += "12 heures à 13 heures par " + nm + "\n"
                        form_5_obj.save()
                if tz.upper() == "OK":
                    if form_5_obj is None:
                        form_5_obj = form_5.objects.get(id = 7)
                        form_5_obj.lundi += "13 heures à 14 heures par " + nm + "\n"
                        form_5_obj.save()
                    else:
                        form_5_obj = form_5.objects.get(id = 7)
                        form_5_obj.lundi += "13 heures à 14 heures par " + nm + "\n"
                        form_5_obj.save()
                if qaz.upper() == "OK":
                    if form_5_obj is None:
                        form_5_obj = form_5.objects.get(id = 6)
                        form_5_obj.lundi += "14 heures à 15 heures par " + nm + "\n"
                        form_5_obj.save()
                    else:
                        form_5_obj = form_5.objects.get(id = 6)
                        form_5_obj.lundi += "14 heures à 15 heures par " + nm + "\n"
                        form_5_obj.save()
                if qiz.upper() == "OK":
                    if form_5_obj is None:
                        form_5_obj = form_5.objects.get(id = 5)
                        form_5_obj.lundi += "15 heures à 16 heures par " + nm + "\n"
                        form_5_obj.save()
                    else:
                        form_5_obj = form_5.objects.get(id = 5)
                        form_5_obj.lundi += "15 heures à 16 heures par " + nm + "\n"
                        form_5_obj.save()
                if sz.upper() == "OK":
                    if form_5_obj is None:
                        form_5_obj = form_5.objects.get(id = 4)
                        form_5_obj.lundi += "16 heures à 17 heures par " + nm + "\n"
                        form_5_obj.save()
                    else:
                        form_5_obj = form_5.objects.get(id = 4)
                        form_5_obj.lundi += "16 heures à 17 heures par " + nm + "\n"
                        form_5_obj.save()
                if ds.upper() == "OK":
                    if form_5_obj is None:
                        form_5_obj = form_5.objects.get(id = 3)
                        form_5_obj.lundi += "17 heures à 18 heures par " + nm + "\n"
                        form_5_obj.save()
                    else:
                        form_5_obj = form_5.objects.get(id = 3)
                        form_5_obj.lundi += "17 heures à 18 heures par " + nm + "\n"
                        form_5_obj.save()          
                if dht.upper() == "OK":
                    if form_5_obj is None:
                        form_5_obj = form_5.objects.get(id = 2)
                        form_5_obj.lundi += "18 heures à 19 heures par " + nm + "\n"
                        form_5_obj.save()
                    else:
                        form_5_obj = form_5.objects.get(id = 2)
                        form_5_obj.lundi += "18 heures à 19 heures par " + nm + "\n"
                        form_5_obj.save()
                if dnf.upper() == "OK":
                    if form_5_obj is None:
                        form_5_obj = form_5.objects.get(id = 1)
                        form_5_obj.lundi += "19 heures à 20 heures par " + nm + "\n"
                        form_5_obj.save()
                    else:
                        form_5_obj = form_5.objects.get(id = 1)
                        form_5_obj.lundi += "19 heures à 20 heures par " + nm + "\n"
                        form_5_obj.save()
                

            if jr.upper() == "MARDI":
                if st.upper() == "OK":
                    if form_5_obj is None:
                        form_5_obj = form_5.objects.get(id = 13)
                        form_5_obj.mardi += "7 heures à 8 heures par " + nm + "\n"
                        form_5_obj.save()
                    else:
                        form_5_obj = form_5.objects.get(id = 13)
                        form_5_obj.mardi += "7 heures à 8 heures par " + nm + "\n"
                        form_5_obj.save()
                if ht.upper() == "OK":
                    if form_5_obj is None:
                        form_5_obj = form_5.objects.get(id = 12)
                        form_5_obj.mardi += "8 heures à 9 heures par " + nm + "\n"
                        form_5_obj.save()
                    else:
                        form_5_obj = form_5.objects.get(id = 12)
                        form_5_obj.mardi += "8 heures à 9 heures par " + nm + "\n"
                        form_5_obj.save()
                if nf.upper() == "OK":
                    if form_5_obj is None:
                        form_5_obj = form_5.objects.get(id = 11)
                        form_5_obj.mardi += "9 heures à 10 heures par " + nm + "\n"
                        form_5_obj.save()
                    else:
                        form_5_obj = form_5.objects.get(id = 11)
                        form_5_obj.mardi += "9 heures à 10 heures par " + nm + "\n"
                        form_5_obj.save()
                if dx.upper() == "OK":
                    if form_5_obj is None:
                        form_5_obj = form_5.objects.get(id = 10)
                        form_5_obj.mardi += "10 heures à 11 heures par " + nm + "\n"
                        form_5_obj.save()
                    else:
                        form_5_obj = form_5.objects.get(id = 10)
                        form_5_obj.mardi += "10 heures à 11 heures par " + nm + "\n"
                        form_5_obj.save()
                if oz.upper() == "OK":
                    if form_5_obj is None:
                        form_5_obj = form_5.objects.get(id = 9)
                        form_5_obj.mardi += "11 heures à 12 heures par " + nm + "\n"
                        form_5_obj.save()
                    else:
                        form_5_obj = form_5.objects.get(id = 9)
                        form_5_obj.mardi += "11 heures à 12 heures par " + nm + "\n"
                        form_5_obj.save()
                if dz.upper() == "OK":
                    if form_5_obj is None:
                        form_5_obj = form_5.objects.get(id = 8)
                        form_5_obj.mardi += "12 heures à 13 heures par " + nm + "\n"
                        form_5_obj.save()
                    else:
                        form_5_obj = form_5.objects.get(id = 8)
                        form_5_obj.mardi += "12 heures à 13 heures par " + nm + "\n"
                        form_5_obj.save()
                if tz.upper() == "OK":
                    if form_5_obj is None:
                        form_5_obj = form_5.objects.get(id = 7)
                        form_5_obj.mardi += "13 heures à 14 heures par " + nm + "\n"
                        form_5_obj.save()
                    else:
                        form_5_obj = form_5.objects.get(id = 7)
                        form_5_obj.mardi += "13 heures à 14 heures par " + nm + "\n"
                        form_5_obj.save()
                if qaz.upper() == "OK":
                    if form_5_obj is None:
                        form_5_obj = form_5.objects.get(id = 6)
                        form_5_obj.mardi += "14 heures à 15 heures par " + nm + "\n"
                        form_5_obj.save()
                    else:
                        form_5_obj = form_5.objects.get(id = 6)
                        form_5_obj.mardi += "14 heures à 15 heures par " + nm + "\n"
                        form_5_obj.save()
                if qiz.upper() == "OK":
                    if form_5_obj is None:
                        form_5_obj = form_5.objects.get(id = 5)
                        form_5_obj.mardi += "15 heures à 16 heures par " + nm + "\n"
                        form_5_obj.save()
                    else:
                        form_5_obj = form_5.objects.get(id = 5)
                        form_5_obj.mardi += "15 heures à 16 heures par " + nm + "\n"
                        form_5_obj.save()
                if sz.upper() == "OK":
                    if form_5_obj is None:
                        form_5_obj = form_5.objects.get(id = 4)
                        form_5_obj.mardi += "16 heures à 17 heures par " + nm + "\n"
                        form_5_obj.save()
                    else:
                        form_5_obj = form_5.objects.get(id = 4)
                        form_5_obj.mardi += "16 heures à 17 heures par " + nm + "\n"
                        form_5_obj.save()
                if ds.upper() == "OK":
                    if form_5_obj is None:
                        form_5_obj = form_5.objects.get(id = 3)
                        form_5_obj.mardi += "17 heures à 18 heures par " + nm + "\n"
                        form_5_obj.save()
                    else:
                        form_5_obj = form_5.objects.get(id = 3)
                        form_5_obj.mardi += "17 heures à 18 heures par " + nm + "\n"
                        form_5_obj.save()          
                if dht.upper() == "OK":
                    if form_5_obj is None:
                        form_5_obj = form_5.objects.get(id = 2)
                        form_5_obj.mardi += "18 heures à 19 heures par " + nm + "\n"
                        form_5_obj.save()
                    else:
                        form_5_obj = form_5.objects.get(id = 2)
                        form_5_obj.mardi += "18 heures à 19 heures par " + nm + "\n"
                        form_5_obj.save()
                if dnf.upper() == "OK":
                    if form_5_obj is None:
                        form_5_obj = form_5.objects.get(id = 1)
                        form_5_obj.mardi += "19 heures à 20 heures par " + nm + "\n"
                        form_5_obj.save()
                    else:
                        form_5_obj = form_5.objects.get(id = 1)
                        form_5_obj.mardi += "19 heures à 20 heures par " + nm + "\n"
                        form_5_obj.save()


            if jr.upper() == "MERCREDI":
                if st.upper() == "OK":
                    if form_5_obj is None:
                        form_5_obj = form_5.objects.get(id = 13)
                        form_5_obj.mercredi += "7 heures à 8 heures par " + nm + "\n"
                        form_5_obj.save()
                    else:
                        form_5_obj = form_5.objects.get(id = 13)
                        form_5_obj.mercredi += "7 heures à 8 heures par " + nm + "\n"
                        form_5_obj.save()
                if ht.upper() == "OK":
                    if form_5_obj is None:
                        form_5_obj = form_5.objects.get(id = 12)
                        form_5_obj.mercredi += "8 heures à 9 heures par " + nm + "\n"
                        form_5_obj.save()
                    else:
                        form_5_obj = form_5.objects.get(id = 12)
                        form_5_obj.mercredi += "8 heures à 9 heures par " + nm + "\n"
                        form_5_obj.save()
                if nf.upper() == "OK":
                    if form_5_obj is None:
                        form_5_obj = form_5.objects.get(id = 11)
                        form_5_obj.mercredi += "9 heures à 10 heures par " + nm + "\n"
                        form_5_obj.save()
                    else:
                        form_5_obj = form_5.objects.get(id = 11)
                        form_5_obj.mercredi += "9 heures à 10 heures par " + nm + "\n"
                        form_5_obj.save()
                if dx.upper() == "OK":
                    if form_5_obj is None:
                        form_5_obj = form_5.objects.get(id = 10)
                        form_5_obj.mercredi += "10 heures à 11 heures par " + nm + "\n"
                        form_5_obj.save()
                    else:
                        form_5_obj = form_5.objects.get(id = 10)
                        form_5_obj.mercredi += "10 heures à 11 heures par " + nm + "\n"
                        form_5_obj.save()
                if oz.upper() == "OK":
                    if form_5_obj is None:
                        form_5_obj = form_5.objects.get(id = 9)
                        form_5_obj.mercredi += "11 heures à 12 heures par " + nm + "\n"
                        form_5_obj.save()
                    else:
                        form_5_obj = form_5.objects.get(id = 9)
                        form_5_obj.mercredi += "11 heures à 12 heures par " + nm + "\n"
                        form_5_obj.save()
                if dz.upper() == "OK":
                    if form_5_obj is None:
                        form_5_obj = form_5.objects.get(id = 8)
                        form_5_obj.mercredi += "12 heures à 13 heures par " + nm + "\n"
                        form_5_obj.save()
                    else:
                        form_5_obj = form_5.objects.get(id = 8)
                        form_5_obj.mercredi += "12 heures à 13 heures par " + nm + "\n"
                        form_5_obj.save()
                if tz.upper() == "OK":
                    if form_5_obj is None:
                        form_5_obj = form_5.objects.get(id = 7)
                        form_5_obj.mercredi += "13 heures à 14 heures par " + nm + "\n"
                        form_5_obj.save()
                    else:
                        form_5_obj = form_5.objects.get(id = 7)
                        form_5_obj.mercredi += "13 heures à 14 heures par " + nm + "\n"
                        form_5_obj.save()
                if qaz.upper() == "OK":
                    if form_5_obj is None:
                        form_5_obj = form_5.objects.get(id = 6)
                        form_5_obj.mercredi += "14 heures à 15 heures par " + nm + "\n"
                        form_5_obj.save()
                    else:
                        form_5_obj = form_5.objects.get(id = 6)
                        form_5_obj.mercredi += "14 heures à 15 heures par " + nm + "\n"
                        form_5_obj.save()
                if qiz.upper() == "OK":
                    if form_5_obj is None:
                        form_5_obj = form_5.objects.get(id = 5)
                        form_5_obj.mercredi += "15 heures à 16 heures par " + nm + "\n"
                        form_5_obj.save()
                    else:
                        form_5_obj = form_5.objects.get(id = 5)
                        form_5_obj.mercredi += "15 heures à 16 heures par " + nm + "\n"
                        form_5_obj.save()
                if sz.upper() == "OK":
                    if form_5_obj is None:
                        form_5_obj = form_5.objects.get(id = 4)
                        form_5_obj.mercredi += "16 heures à 17 heures par " + nm + "\n"
                        form_5_obj.save()
                    else:
                        form_5_obj = form_5.objects.get(id = 4)
                        form_5_obj.mercredi += "16 heures à 17 heures par " + nm + "\n"
                        form_5_obj.save()
                if ds.upper() == "OK":
                    if form_5_obj is None:
                        form_5_obj = form_5.objects.get(id = 3)
                        form_5_obj.mercredi += "17 heures à 18 heures par " + nm + "\n"
                        form_5_obj.save()
                    else:
                        form_5_obj = form_5.objects.get(id = 3)
                        form_5_obj.mercredi += "17 heures à 18 heures par " + nm + "\n"
                        form_5_obj.save()          
                if dht.upper() == "OK":
                    if form_5_obj is None:
                        form_5_obj = form_5.objects.get(id = 2)
                        form_5_obj.mercredi += "18 heures à 19 heures par " + nm + "\n"
                        form_5_obj.save()
                    else:
                        form_5_obj = form_5.objects.get(id = 2)
                        form_5_obj.mercredi += "18 heures à 19 heures par " + nm + "\n"
                        form_5_obj.save()
                if dnf.upper() == "OK":
                    if form_5_obj is None:
                        form_5_obj = form_5.objects.get(id = 1)
                        form_5_obj.mercredi += "19 heures à 20 heures par " + nm + "\n"
                        form_5_obj.save()
                    else:
                        form_5_obj = form_5.objects.get(id = 1)
                        form_5_obj.mercredi += "19 heures à 20 heures par " + nm + "\n"
                        form_5_obj.save()

            
            if jr.upper() == "JEUDI":
                if st.upper() == "OK":
                    if form_5_obj is None:
                        form_5_obj = form_5.objects.get(id = 13)
                        form_5_obj.jeudi += "7 heures à 8 heures par " + nm + "\n"
                        form_5_obj.save()
                    else:
                        form_5_obj = form_5.objects.get(id = 13)
                        form_5_obj.jeudi += "7 heures à 8 heures par " + nm + "\n"
                        form_5_obj.save()
                if ht.upper() == "OK":
                    if form_5_obj is None:
                        form_5_obj = form_5.objects.get(id = 12)
                        form_5_obj.jeudi += "8 heures à 9 heures par " + nm + "\n"
                        form_5_obj.save()
                    else:
                        form_5_obj = form_5.objects.get(id = 12)
                        form_5_obj.jeudi += "8 heures à 9 heures par " + nm + "\n"
                        form_5_obj.save()
                if nf.upper() == "OK":
                    if form_5_obj is None:
                        form_5_obj = form_5.objects.get(id = 11)
                        form_5_obj.jeudi += "9 heures à 10 heures par " + nm + "\n"
                        form_5_obj.save()
                    else:
                        form_5_obj = form_5.objects.get(id = 11)
                        form_5_obj.jeudi += "9 heures à 10 heures par " + nm + "\n"
                        form_5_obj.save()
                if dx.upper() == "OK":
                    if form_5_obj is None:
                        form_5_obj = form_5.objects.get(id = 10)
                        form_5_obj.jeudi += "10 heures à 11 heures par " + nm + "\n"
                        form_5_obj.save()
                    else:
                        form_5_obj = form_5.objects.get(id = 10)
                        form_5_obj.jeudi += "10 heures à 11 heures par " + nm + "\n"
                        form_5_obj.save()
                if oz.upper() == "OK":
                    if form_5_obj is None:
                        form_5_obj = form_5.objects.get(id = 9)
                        form_5_obj.jeudi += "11 heures à 12 heures par " + nm + "\n"
                        form_5_obj.save()
                    else:
                        form_5_obj = form_5.objects.get(id = 9)
                        form_5_obj.jeudi += "11 heures à 12 heures par " + nm + "\n"
                        form_5_obj.save()
                if dz.upper() == "OK":
                    if form_5_obj is None:
                        form_5_obj = form_5.objects.get(id = 8)
                        form_5_obj.jeudi += "12 heures à 13 heures par " + nm + "\n"
                        form_5_obj.save()
                    else:
                        form_5_obj = form_5.objects.get(id = 8)
                        form_5_obj.jeudi += "12 heures à 13 heures par " + nm + "\n"
                        form_5_obj.save()
                if tz.upper() == "OK":
                    if form_5_obj is None:
                        form_5_obj = form_5.objects.get(id = 7)
                        form_5_obj.jeudi += "13 heures à 14 heures par " + nm + "\n"
                        form_5_obj.save()
                    else:
                        form_5_obj = form_5.objects.get(id = 7)
                        form_5_obj.jeudi += "13 heures à 14 heures par " + nm + "\n"
                        form_5_obj.save()
                if qaz.upper() == "OK":
                    if form_5_obj is None:
                        form_5_obj = form_5.objects.get(id = 6)
                        form_5_obj.jeudi += "14 heures à 15 heures par " + nm + "\n"
                        form_5_obj.save()
                    else:
                        form_5_obj = form_5.objects.get(id = 6)
                        form_5_obj.jeudi += "14 heures à 15 heures par " + nm + "\n"
                        form_5_obj.save()
                if qiz.upper() == "OK":
                    if form_5_obj is None:
                        form_5_obj = form_5.objects.get(id = 5)
                        form_5_obj.jeudi += "15 heures à 16 heures par " + nm + "\n"
                        form_5_obj.save()
                    else:
                        form_5_obj = form_5.objects.get(id = 5)
                        form_5_obj.jeudi += "15 heures à 16 heures par " + nm + "\n"
                        form_5_obj.save()
                if sz.upper() == "OK":
                    if form_5_obj is None:
                        form_5_obj = form_5.objects.get(id = 4)
                        form_5_obj.jeudi += "16 heures à 17 heures par " + nm + "\n"
                        form_5_obj.save()
                    else:
                        form_5_obj = form_5.objects.get(id = 4)
                        form_5_obj.jeudi += "16 heures à 17 heures par " + nm + "\n"
                        form_5_obj.save()
                if ds.upper() == "OK":
                    if form_5_obj is None:
                        form_5_obj = form_5.objects.get(id = 3)
                        form_5_obj.jeudi += "17 heures à 18 heures par " + nm + "\n"
                        form_5_obj.save()
                    else:
                        form_5_obj = form_5.objects.get(id = 3)
                        form_5_obj.jeudi += "17 heures à 18 heures par " + nm + "\n"
                        form_5_obj.save()          
                if dht.upper() == "OK":
                    if form_5_obj is None:
                        form_5_obj = form_5.objects.get(id = 2)
                        form_5_obj.jeudi += "18 heures à 19 heures par " + nm + "\n"
                        form_5_obj.save()
                    else:
                        form_5_obj = form_5.objects.get(id = 2)
                        form_5_obj.jeudi += "18 heures à 19 heures par " + nm + "\n"
                        form_5_obj.save()
                if dnf.upper() == "OK":
                    if form_5_obj is None:
                        form_5_obj = form_5.objects.get(id = 1)
                        form_5_obj.jeudi += "19 heures à 20 heures par " + nm + "\n"
                        form_5_obj.save()
                    else:
                        form_5_obj = form_5.objects.get(id = 1)
                        form_5_obj.jeudi += "19 heures à 20 heures par " + nm + "\n"
                        form_5_obj.save()

            if jr.upper() == "VENDREDI":
                if st.upper() == "OK":
                    if form_5_obj is None:
                        form_5_obj = form_5.objects.get(id = 13)
                        form_5_obj.vendredi += "7 heures à 8 heures par " + nm + "\n"
                        form_5_obj.save()
                    else:
                        form_5_obj = form_5.objects.get(id = 13)
                        form_5_obj.vendredi += "7 heures à 8 heures par " + nm + "\n"
                        form_5_obj.save()
                if ht.upper() == "OK":
                    if form_5_obj is None:
                        form_5_obj = form_5.objects.get(id = 12)
                        form_5_obj.vendredi += "8 heures à 9 heures par " + nm + "\n"
                        form_5_obj.save()
                    else:
                        form_5_obj = form_5.objects.get(id = 12)
                        form_5_obj.vendredi += "8 heures à 9 heures par " + nm + "\n"
                        form_5_obj.save()
                if nf.upper() == "OK":
                    if form_5_obj is None:
                        form_5_obj = form_5.objects.get(id = 11)
                        form_5_obj.vendredi += "9 heures à 10 heures par " + nm + "\n"
                        form_5_obj.save()
                    else:
                        form_5_obj = form_5.objects.get(id = 11)
                        form_5_obj.vendredi += "9 heures à 10 heures par " + nm + "\n"
                        form_5_obj.save()
                if dx.upper() == "OK":
                    if form_5_obj is None:
                        form_5_obj = form_5.objects.get(id = 10)
                        form_5_obj.vendredi += "10 heures à 11 heures par " + nm + "\n"
                        form_5_obj.save()
                    else:
                        form_5_obj = form_5.objects.get(id = 10)
                        form_5_obj.vendredi += "10 heures à 11 heures par " + nm + "\n"
                        form_5_obj.save()
                if oz.upper() == "OK":
                    if form_5_obj is None:
                        form_5_obj = form_5.objects.get(id = 9)
                        form_5_obj.vendredi += "11 heures à 12 heures par " + nm + "\n"
                        form_5_obj.save()
                    else:
                        form_5_obj = form_5.objects.get(id = 9)
                        form_5_obj.vendredi += "11 heures à 12 heures par " + nm + "\n"
                        form_5_obj.save()
                if dz.upper() == "OK":
                    if form_5_obj is None:
                        form_5_obj = form_5.objects.get(id = 8)
                        form_5_obj.vendredi += "12 heures à 13 heures par " + nm + "\n"
                        form_5_obj.save()
                    else:
                        form_5_obj = form_5.objects.get(id = 8)
                        form_5_obj.vendredi += "12 heures à 13 heures par " + nm + "\n"
                        form_5_obj.save()
                if tz.upper() == "OK":
                    if form_5_obj is None:
                        form_5_obj = form_5.objects.get(id = 7)
                        form_5_obj.vendredi += "13 heures à 14 heures par " + nm + "\n"
                        form_5_obj.save()
                    else:
                        form_5_obj = form_5.objects.get(id = 7)
                        form_5_obj.vendredi += "13 heures à 14 heures par " + nm + "\n"
                        form_5_obj.save()
                if qaz.upper() == "OK":
                    if form_5_obj is None:
                        form_5_obj = form_5.objects.get(id = 6)
                        form_5_obj.vendredi += "14 heures à 15 heures par " + nm + "\n"
                        form_5_obj.save()
                    else:
                        form_5_obj = form_5.objects.get(id = 6)
                        form_5_obj.vendredi += "14 heures à 15 heures par " + nm + "\n"
                        form_5_obj.save()
                if qiz.upper() == "OK":
                    if form_5_obj is None:
                        form_5_obj = form_5.objects.get(id = 5)
                        form_5_obj.vendredi += "15 heures à 16 heures par " + nm + "\n"
                        form_5_obj.save()
                    else:
                        form_5_obj = form_5.objects.get(id = 5)
                        form_5_obj.vendredi += "15 heures à 16 heures par " + nm + "\n"
                        form_5_obj.save()
                if sz.upper() == "OK":
                    if form_5_obj is None:
                        form_5_obj = form_5.objects.get(id = 4)
                        form_5_obj.vendredi += "16 heures à 17 heures par " + nm + "\n"
                        form_5_obj.save()
                    else:
                        form_5_obj = form_5.objects.get(id = 4)
                        form_5_obj.vendredi += "16 heures à 17 heures par " + nm + "\n"
                        form_5_obj.save()
                if ds.upper() == "OK":
                    if form_5_obj is None:
                        form_5_obj = form_5.objects.get(id = 3)
                        form_5_obj.vendredi += "17 heures à 18 heures par " + nm + "\n"
                        form_5_obj.save()
                    else:
                        form_5_obj = form_5.objects.get(id = 3)
                        form_5_obj.vendredi += "17 heures à 18 heures par " + nm + "\n"
                        form_5_obj.save()          
                if dht.upper() == "OK":
                    if form_5_obj is None:
                        form_5_obj = form_5.objects.get(id = 2)
                        form_5_obj.vendredi += "18 heures à 19 heures par " + nm + "\n"
                        form_5_obj.save()
                    else:
                        form_5_obj = form_5.objects.get(id = 2)
                        form_5_obj.vendredi += "18 heures à 19 heures par " + nm + "\n"
                        form_5_obj.save()
                if dnf.upper() == "OK":
                    if form_5_obj is None:
                        form_5_obj = form_5.objects.get(id = 1)
                        form_5_obj.vendredi += "19 heures à 20 heures par " + nm + "\n"
                        form_5_obj.save()
                    else:
                        form_5_obj = form_5.objects.get(id = 1)
                        form_5_obj.vendredi += "19 heures à 20 heures par " + nm + "\n"
                        form_5_obj.save()
            
            if jr.upper() == "SAMEDI":
                if st.upper() == "OK":
                    if form_5_obj is None:
                        form_5_obj = form_5.objects.get(id = 13)
                        form_5_obj.samedi += "7 heures à 8 heures par " + nm + "\n"
                        form_5_obj.save()
                    else:
                        form_5_obj = form_5.objects.get(id = 13)
                        form_5_obj.samedi += "7 heures à 8 heures par " + nm + "\n"
                        form_5_obj.save()
                if ht.upper() == "OK":
                    if form_5_obj is None:
                        form_5_obj = form_5.objects.get(id = 12)
                        form_5_obj.samedi += "8 heures à 9 heures par " + nm + "\n"
                        form_5_obj.save()
                    else:
                        form_5_obj = form_5.objects.get(id = 12)
                        form_5_obj.samedi += "8 heures à 9 heures par " + nm + "\n"
                        form_5_obj.save()
                if nf.upper() == "OK":
                    if form_5_obj is None:
                        form_5_obj = form_5.objects.get(id = 11)
                        form_5_obj.samedi += "9 heures à 10 heures par " + nm + "\n"
                        form_5_obj.save()
                    else:
                        form_5_obj = form_5.objects.get(id = 11)
                        form_5_obj.samedi += "9 heures à 10 heures par " + nm + "\n"
                        form_5_obj.save()
                if dx.upper() == "OK":
                    if form_5_obj is None:
                        form_5_obj = form_5.objects.get(id = 10)
                        form_5_obj.samedi += "10 heures à 11 heures par " + nm + "\n"
                        form_5_obj.save()
                    else:
                        form_5_obj = form_5.objects.get(id = 10)
                        form_5_obj.samedi += "10 heures à 11 heures par " + nm + "\n"
                        form_5_obj.save()
                if oz.upper() == "OK":
                    if form_5_obj is None:
                        form_5_obj = form_5.objects.get(id = 9)
                        form_5_obj.samedi += "11 heures à 12 heures par " + nm + "\n"
                        form_5_obj.save()
                    else:
                        form_5_obj = form_5.objects.get(id = 9)
                        form_5_obj.samedi += "11 heures à 12 heures par " + nm + "\n"
                        form_5_obj.save()
                if dz.upper() == "OK":
                    if form_5_obj is None:
                        form_5_obj = form_5.objects.get(id = 8)
                        form_5_obj.samedi += "12 heures à 13 heures par " + nm + "\n"
                        form_5_obj.save()
                    else:
                        form_5_obj = form_5.objects.get(id = 8)
                        form_5_obj.samedi += "12 heures à 13 heures par " + nm + "\n"
                        form_5_obj.save()
                if tz.upper() == "OK":
                    if form_5_obj is None:
                        form_5_obj = form_5.objects.get(id = 7)
                        form_5_obj.samedi += "13 heures à 14 heures par " + nm + "\n"
                        form_5_obj.save()
                    else:
                        form_5_obj = form_5.objects.get(id = 7)
                        form_5_obj.samedi += "13 heures à 14 heures par " + nm + "\n"
                        form_5_obj.save()
                if qaz.upper() == "OK":
                    if form_5_obj is None:
                        form_5_obj = form_5.objects.get(id = 6)
                        form_5_obj.samedi += "14 heures à 15 heures par " + nm + "\n"
                        form_5_obj.save()
                    else:
                        form_5_obj = form_5.objects.get(id = 6)
                        form_5_obj.samedi += "14 heures à 15 heures par " + nm + "\n"
                        form_5_obj.save()
                if qiz.upper() == "OK":
                    if form_5_obj is None:
                        form_5_obj = form_5.objects.get(id = 5)
                        form_5_obj.samedi += "15 heures à 16 heures par " + nm + "\n"
                        form_5_obj.save()
                    else:
                        form_5_obj = form_5.objects.get(id = 5)
                        form_5_obj.samedi += "15 heures à 16 heures par " + nm + "\n"
                        form_5_obj.save()
                if sz.upper() == "OK":
                    if form_5_obj is None:
                        form_5_obj = form_5.objects.get(id = 4)
                        form_5_obj.samedi += "16 heures à 17 heures par " + nm + "\n"
                        form_5_obj.save()
                    else:
                        form_5_obj = form_5.objects.get(id = 4)
                        form_5_obj.samedi += "16 heures à 17 heures par " + nm + "\n"
                        form_5_obj.save()
                if ds.upper() == "OK":
                    if form_5_obj is None:
                        form_5_obj = form_5.objects.get(id = 3)
                        form_5_obj.samedi += "17 heures à 18 heures par " + nm + "\n"
                        form_5_obj.save()
                    else:
                        form_5_obj = form_5.objects.get(id = 3)
                        form_5_obj.samedi += "17 heures à 18 heures par " + nm + "\n"
                        form_5_obj.save()          
                if dht.upper() == "OK":
                    if form_5_obj is None:
                        form_5_obj = form_5.objects.get(id = 2)
                        form_5_obj.samedi += "18 heures à 19 heures par " + nm + "\n"
                        form_5_obj.save()
                    else:
                        form_5_obj = form_5.objects.get(id = 2)
                        form_5_obj.samedi += "18 heures à 19 heures par " + nm + "\n"
                        form_5_obj.save()
                if dnf.upper() == "OK":
                    if form_5_obj is None:
                        form_5_obj = form_5.objects.get(id = 1)
                        form_5_obj.samedi += "19 heures à 20 heures par " + nm + "\n"
                        form_5_obj.save()
                    else:
                        form_5_obj = form_5.objects.get(id = 1)
                        form_5_obj.samedi += "19 heures à 20 heures par " + nm + "\n"
                        form_5_obj.save()


            if "LUNDI" in jr.upper():
                Pass = jr.upper()
                fm = StudentRegistration3()
                return render(request, 'Etudiant/pre_remplissage.html', {'Pass': Pass, "form": fm, 'name': nm})
            elif "MARDI" in jr.upper():
                Pass = jr.upper()
                fm = StudentRegistration3()
                return render(request, 'Etudiant/pre_remplissage.html', {'Pass': Pass, "form": fm, 'name': nm})
            elif "MERCREDI" in jr.upper():
                Pass = jr.upper()
                fm = StudentRegistration3()
                return render(request, 'Etudiant/pre_remplissage.html', {'Pass': Pass, "form": fm, 'name': nm})
            elif "JEUDI" in jr.upper():
                Pass = jr.upper()
                fm = StudentRegistration3()
                return render(request, 'Etudiant/pre_remplissage.html', {'Pass': Pass, "form": fm, 'name': nm})
            elif "VENDREDI" in jr.upper():
                Pass = jr.upper()
                fm = StudentRegistration3()
                return render(request, 'Etudiant/pre_remplissage.html', {'Pass': Pass, "form": fm, 'name': nm})
            elif "SAMEDI" in jr.upper():
                Pass = jr.upper()
                fm = StudentRegistration3()
                return render(request, 'Etudiant/pre_remplissage.html', {'Pass': Pass, "form": fm, 'name': nm})
            else:
                information = "Choisissez s'il vous plait un jour entre ceux affichés ci-dessus !\n Ecrivez-les conformément."
                return render(request, 'Etudiant/pre_remplissage.html', {'form': fm, 'information':information})
    else:
        fm = StudentRegistration3()
    return render(request, 'Etudiant/pre_remplissage.html', {'form': fm})









"""

                if 'PROF' in st.upper():
                    form_2_obj = form_2.objects.first()  # Récupèration de l'instance de mon form_2 existante
                    if form_2_obj is None:
                        form_2(permission='okokok').save()  # Création d'une nouvelle instance de form_2 avec permission='okokok'
                    else:
                        form_2_obj.permission = 'okokok'
                        form_2_obj.save()
                else:
                    form_2_obj = form_2.objects.first()  # Récupèration de l'instance de mon form_2 existante
                    if form_2_obj is None:
                        form_2(permission='ikikik').save()  # Création d'une nouvelle instance de form_2 avec permission='ikikik'
                    else:
                        form_2_obj.permission = 'ikikik'
                        form_2_obj.save()
                messages.warning(request, "Ravi de vous revoir !")
                return redirect('professeur')

"""