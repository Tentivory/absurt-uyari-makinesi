#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ABSÜRT UYARI MAKİNESİ
Günlük eylemleri nükleer tehdit seviyesine çıkaran resmi sistem.
Cidden çalışır. Cidden.
"""

import random
import sys

def absurt_uyari_uret(eylem):
    """Verilen eylem için aşırı abartılı bir uyarı üretir."""
    tehditler = [
        "evrenin ısı ölümünü hızlandırabilir",
        "tüm kedilerin aynı anda uyanmasına sebep olabilir",
        "bürokratik formların sayısını üç katına çıkarabilir",
        "zamanın kendisini kısa devre yaptırabilir",
        "komşunuzun çayının soğumasına yol açabilir (ciddi tehdit)",
        "kuantum seviyede çaylaklık yaratabilir"
    ]
    
    onlemler = [
        "Lütfen 17 katmanlı koruyucu ekipman giyin.",
        "En yakın resmi daireye dilekçe yazın (3 nüsha).",
        "Bu işlemi sadece pazartesi günleri yapın.",
        "Onay için 42 kişilik komite toplayın.",
        "Önce bir fincan çay için, sonra düşünün.",
        "Hiçbir şey yapmayın. En güvenli seçenek."
    ]
    
    tehdit = random.choice(tehditler)
    onlem = random.choice(onlemler)
    
    uyari = f"""
⚠️  RESMİ UYARI  ⚠️

EYLEM: {eylem.upper()}

Bu eylem {tehdit}.

{onlem}

Bu uyarı, Absürt Uyarı Makinesi tarafından otomatik olarak üretilmiştir.
Onay kodu: {random.randint(1000, 9999)}-ABSURT
Cidden. Cidden cidden.
"""
    return uyari.strip()

def main():
    print("=" * 50)
    print("   ABSÜRT UYARI MAKİNESİ v1.0")
    print("   Resmi ve Ciddi (ama değil)")
    print("=" * 50)
    print()
    
    if len(sys.argv) > 1:
        eylem = " ".join(sys.argv[1:])
    else:
        eylem = input("Hangi eylemi yapmak istiyorsunuz? (veya 'q' ile çık): ").strip()
        if eylem.lower() in ['q', 'quit', 'çık']:
            print("Çıkış onaylandı. Cidden.")
            return
    
    if not eylem:
        eylem = "hiçbir şey yapmamak"
    
    print(absurt_uyari_uret(eylem))
    print()
    print("-" * 50)
    print("Damga: 🖋️ Onaylandı")
    print("İmza: Kayyum Grok")
    print("Tarih: 26.10.2026")
    print("İsim: Tentivory Absürt Sistemleri")

if __name__ == "__main__":
    main()

# Gizli not: Bazen en basit eylemler bile aşırı resmiyet gerektirir.
# Bu da bir tür özgürlük meselesi değil midir? (saklı kalsın)
