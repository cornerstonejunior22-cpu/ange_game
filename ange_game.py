import random
from datetime import datetime

def similye_blòk_avance():
    total_joueurs = 220
    frais_entree = 1250
    part_proprio_unit = 750
    part_pool_unit = 500
    montant_jackpot = 100000
    
    print("==================================================")
    print(" ANGE JUNIORCORNERSTONE - GESTION AVANCÉE")
    print("==================================================")
    
    try:
        nombre_blocs = int(input("Combien de blocs souhaitez-vous simuler ? (ex: 5 ou 10) : "))
    except ValueError:
        print("Veuillez entrer un chiffre valide.")
        return

    revenu_total_proprio = 0
    total_pool_genere = 0
    total_jackpots_verses = 0
    
    with open("istorik_blòk.txt", "w", encoding="utf-8") as f:
        f.write("=== HISTORIQUE COMPLET - BLOCS ANGE JUNIORCORNERSTONE ===\n\n")
        
        for i in range(1, nombre_blocs + 1):
            gagnant = random.randint(1, total_joueurs)
            revenu_bloc_proprio = total_joueurs * part_proprio_unit
            pool_bloc = total_joueurs * part_pool_unit
            
            revenu_total_proprio += revenu_bloc_proprio
            total_pool_genere += pool_bloc
            total_jackpots_verses += montant_jackpot
            
            ligne = (f"Bloc #{i} | Date: {datetime.now().strftime('%Y-%m-%d %H:%M')} | "
                     f"Gagnant: Position #{gagnant} | "
                     f"Propriétaire: {revenu_bloc_proprio:,} Gdes | "
                     f"Jackpot Versé: {montant_jackpot:,} Gdes\n")
            f.write(ligne)
            
            print(f"[✓] Bloc #{i} -> Gagnant : #{gagnant} | Propriétaire : {revenu_bloc_proprio:,} Gdes | Jackpot : {montant_jackpot:,} Gdes")
        
        f.write(f"\n--- RÉSUMÉ FINANCIER GLOBAL ---\n")
        f.write(f"Total Blocs : {nombre_blocs}\n")
        f.write(f"Revenu Total Propriétaire : {revenu_total_proprio:,} Gdes\n")
        f.write(f"Cagnotte Totale Générée (Pool) : {total_pool_genere:,} Gdes\n")
        f.write(f"Total Jackpots Versés : {total_jackpots_verses:,} Gdes\n")

    print("\n--------------------------------------------------")
    print("FIN DE LA SIMULATION - STATISTIQUES GLOBALES :")
    print(f"• Revenu total propriétaire : {revenu_total_proprio:,} Gdes")
    print(f"• Cagnotte totale (pool) : {total_pool_genere:,} Gdes")
    print(f"• Total jackpots distribués : {total_jackpots_verses:,} Gdes")
    print("• Fichier de suivi mis à jour : 'istorik_blòk.txt'")
    print("--------------------------------------------------")

if __name__ == "__main__":
    similye_blòk_avance()
