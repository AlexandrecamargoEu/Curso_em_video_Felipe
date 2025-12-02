#!/usr/bin/env python3
"""
Script para testar e verificar as taxas retornadas pelas APIs das exchanges
"""

from binance import Binance
from foxbit import Foxbit
from mercado import Mercado
from novadax import Novadax

def test_exchange_fees():
    """Testa as taxas de todas as exchanges"""
    
    # Par de teste comum
    base = "BTC"
    quote = "USDT"
    
    exchanges = {
        "Binance": Binance(),
        "Foxbit": Foxbit(),
        "Mercado": Mercado(),
        "Novadax": Novadax()
    }
    
    print("=" * 60)
    print("TESTE DE TAXAS DAS EXCHANGES")
    print("=" * 60)
    
    for name, exchange in exchanges.items():
        print(f"\n📊 {name.upper()}")
        print("-" * 30)
        
        try:
            # Testa com diferentes pares
            test_pairs = [
                ("BTC", "USDT"),
                ("ETH", "USDT"), 
                ("PEPE", "BRL"),
                ("BTC", "BRL")
            ]
            
            for test_base, test_quote in test_pairs:
                try:
                    fees = exchange.get_fees(test_base, test_quote)
                    
                    if fees:
                        taker_percent = fees['taker'] * 100
                        maker_percent = fees['maker'] * 100
                        
                        print(f"  {test_base}/{test_quote}:")
                        print(f"    Taker: {fees['taker']:.6f} ({taker_percent:.3f}%)")
                        print(f"    Maker: {fees['maker']:.6f} ({maker_percent:.3f}%)")
                        
                        # Alerta para taxas suspeitas
                        if taker_percent > 2 or maker_percent > 2:
                            print(f"    ⚠️  ALERTA: Taxa muito alta!")
                        
                        break  # Se conseguiu um par, não precisa testar outros
                        
                    else:
                        print(f"    {test_base}/{test_quote}: ❌ Falhou")
                        
                except Exception as e:
                    print(f"    {test_base}/{test_quote}: ❌ Erro: {str(e)}")
                    continue
                    
        except Exception as e:
            print(f"  ❌ Erro geral: {str(e)}")

def test_specific_pair(base="PEPE", quote="BRL"):
    """Testa um par específico em todas as exchanges"""
    
    exchanges = {
        "Binance": Binance(),
        "Foxbit": Foxbit(),
        "Mercado": Mercado(), 
        "Novadax": Novadax()
    }
    
    print(f"\n🔍 TESTE ESPECÍFICO: {base}/{quote}")
    print("=" * 50)
    
    for name, exchange in exchanges.items():
        try:
            fees = exchange.get_fees(base, quote)
            
            if fees:
                print(f"{name:10} | Taker: {fees['taker']:8.6f} | Maker: {fees['maker']:8.6f}")
            else:
                print(f"{name:10} | ❌ Sem dados")
                
        except Exception as e:
            print(f"{name:10} | ❌ Erro: {str(e)}")

def compare_with_documentation():
    """Compara com taxas oficiais da documentação"""
    
    # Taxas oficiais conforme documentação (valores aproximados)
    official_fees = {
        "Binance": {"taker": 0.001, "maker": 0.001},     # 0.1%
        "Foxbit": {"taker": 0.0025, "maker": 0.0025},    # 0.25%  
        "Mercado": {"taker": 0.007, "maker": 0.003},     # 0.7%/0.3%
        "Novadax": {"taker": 0.005, "maker": 0.0025}     # 0.5%/0.25%
    }
    
    exchanges = {
        "Binance": Binance(),
        "Foxbit": Foxbit(),
        "Mercado": Mercado(),
        "Novadax": Novadax()
    }
    
    print("\n📋 COMPARAÇÃO COM DOCUMENTAÇÃO OFICIAL")
    print("=" * 70)
    print(f"{'Exchange':<10} | {'Tipo':<6} | {'API':<10} | {'Oficial':<10} | {'Status'}")
    print("-" * 70)
    
    for name, exchange in exchanges.items():
        try:
            fees = exchange.get_fees("BTC", "USDT")
            official = official_fees[name]
            
            if fees:
                # Taker
                api_taker = fees['taker']
                off_taker = official['taker']
                taker_diff = abs(api_taker - off_taker)
                taker_status = "✅ OK" if taker_diff < 0.001 else f"⚠️ Diff: {taker_diff:.4f}"
                
                print(f"{name:<10} | Taker | {api_taker:<10.6f} | {off_taker:<10.6f} | {taker_status}")
                
                # Maker
                api_maker = fees['maker']
                off_maker = official['maker']
                maker_diff = abs(api_maker - off_maker)
                maker_status = "✅ OK" if maker_diff < 0.001 else f"⚠️ Diff: {maker_diff:.4f}"
                
                print(f"{name:<10} | Maker | {api_maker:<10.6f} | {off_maker:<10.6f} | {maker_status}")
                
            else:
                print(f"{name:<10} | ----- | ❌ API FALHOU")
                
        except Exception as e:
            print(f"{name:<10} | ----- | ❌ ERRO: {str(e)}")

if __name__ == "__main__":
    # Executa todos os testes
    test_exchange_fees()
    test_specific_pair("PEPE", "BRL")
    compare_with_documentation()
    
    print("\n" + "=" * 60)
    print("TESTE CONCLUÍDO")
    print("=" * 60)