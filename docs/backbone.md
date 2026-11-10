# Páteř: jedna otočka Spec Kitu

Provozní manuál základního workflow. Proč je zvolené právě toto, je v [similar-work.md](similar-work.md).

Jedna otočka je jeden běh vestavěného workflow `speckit`. Člověk napíše kartu. Model specifikuje, plánuje, rozdělí úkoly a implementuje. Člověk pustí dál jen specifikaci a plán, které chce. Po implementaci se workflow ukončí. Další otočka je nový běh s novou kartou.

Role, návrh projektu, článek a přenos do praxe tento základ nevolá. Soubory v `agents/` zůstávají v repozitáři jako pozdější rozšíření.

## Princip

1. Jedna otočka má jednu dominantní nejistotu.
2. Trvalý záznam software je jen `.specify/` a `specs/`.
3. Model nesmí sám podat, publikovat, nasadit do cizího provozu ani uzavřít závazek.
4. Provozní ověření je vstup další karty, ne krok uvnitř téhož běhu.
5. Oprava proti aktuální specifikaci zůstává v implementaci. Nová otočka se nezakládá.

## Než začnete

V kořeni projektu, který už má Spec Kit:

```text
specify workflow info speckit
```

Když příkaz workflow nezná, použijte ruční sled níže. Vestavěné workflow na současné dokumentaci Spec Kitu vyžaduje verzi aspoň 0.8.5; integrace `auto` také. Preset tohoto kitu chce `speckit >= 1.0.4`. Rozhoduje výstup `specify version` a `specify workflow info` v daném projektu.

Preset DEV|L je volitelný. Páteř běží i bez něj. S ním specifikace navíc nese pole zralosti; vyplňte je stejnými větami jako kartu a nerozepisujte je podruhé do zbytku `spec.md`.

## Karta otočky

Toto je celý vstup. Čtyři až deset vět. Hypotéza zůstane hypotézou.

```text
Nejistota:
Ověřené (zdroj, datum):
Předpoklad:
Chybí:
Prostředí a co už existuje:
Nejmenší výsledek této otočky:
Odkládá se:
Ověření v provozu (kde, co se bude pozorovat):
```

Volitelný poslední řádek, když pomáhá výběru rozsahu:

```text
Týká se: provozní řetězec | jádro metody | přenos do praxe
```

Když je otočka o zavedení řetězce od dat k výstupu na místě, přečtěte před kartou [field-chain](../skills/field-chain/SKILL.md). Když je o mechanismu a ceně výpočtu, přečtěte [scientific-optimization](../skills/scientific-optimization/SKILL.md). Do karty přidejte jen závěr, který mění specifikaci. Skill workflow nespouští.

## Spuštění

Z kořene projektu, v jednom argumentu celá karta:

```text
specify workflow run speckit -i integration=auto -i spec="<karta>"
```

První brána je specifikace. Otevřete `specs/<feature>/spec.md`. Kontrolujete:

- je tam jedna nejistota a nejmenší výsledek z karty;
- předpoklad není zapsaný jako povinný požadavek;
- odklady jsou mimo rozsah;
- presetová pole, pokud existují, neopakují celou nativní specifikaci.

Schválení:

```text
specify workflow resume <run_id>
```

a volba approve. Odmítnutí běh ukončí. Karta se upraví a běh se spustí znovu.

Druhá brána je plán. Otevřete `plan.md`. Kontrolujete, že odvození a neověřený postup nejsou povinné požadavky a že jednotky, čas a původ dat jsou u práce, které se týkají.

Pak workflow samo spustí úkoly a implementaci.

### Ruční sled

Když `specify workflow` není k dispozici, stejné pořadí v agentovi, se stejnými bránami:

```text
speckit.specify    → člověk zkontroluje spec.md
speckit.plan       → člověk zkontroluje plan.md
speckit.tasks
speckit.implement
```

Mezi specifikací a plánem, pokud je text nejednoznačný, spusťte `speckit.clarify` a teprve pak plán. Mezi plánem a úkoly stejně `speckit.checklist` nebo `speckit.analyze`, když na bráně vidíte mezeru. Po implementaci `speckit.converge`, dokud samotný Spec Kit nehlásí shodu se specifikací. Tyto příkazy nejsou v páteřním workflow, protože ho Spec Kit takto nedodává a pro každou otočku nejsou nutné.

## Po implementaci

Workflow tím končí. Nasazení do reálného provozu je samostatné lidské rozhodnutí.

Další otočka začíná novou kartou. Do „Ověřené“ patří co se v provozu stalo, odkaz na předchozí feature a co z toho plyne. Do „Nejistota“ patří další jedna otázka. Stará specifikace se nepřepisuje, aby nesla nový záměr.

Když výsledek jen nesplňuje aktuální `spec.md`, vraťte se k `speckit.implement` a `speckit.converge`. Novou kartu nezakládejte.

## Co základ záměrně nemá

- Výběr ze čtyř agentů před `specify`.
- Automatický návrh TAČR, rukopis nebo obchodní balík.
- Soubor se zralostí, předávacím protokolem nebo deníkem sezení.
- Větvení workflow podle grade.
- Model, který sám pokračuje z provozu do další feature.

Až karta pravidelně nestačí na jednu z těchto věcí, přidá se jeden specializovaný prompt před tento řetěz. Ne dřív a ne všechny najednou.
