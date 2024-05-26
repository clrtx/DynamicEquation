def dx1t(x1, bpn, bpk, polx3, polx19, polx27, polx21, polx22,polx23,polx29):
    res = (bpn / x1 * polx3 * polx19 * polx27) - (bpk / x1 * polx21 * polx22 * polx23 * polx29)
    return res


def dx2t(x2, mpn, x2x4, polx20, polx28, mpk, polx22, polx23, polx29):
    return (mpn * x2x4 * polx20 * polx28) - (mpk * polx22 * polx23 * polx29)


def dx3t(x3, bv, bz, x3x19, bc):
    res = x3 * ((bv / bz * x3x19) - bc / bv)
    return res


def dx4t(mv, mz, polx20, mc):
    return ((mv / mz * polx20) - (mc / mz))


def dx5t(x5, c, p):
    res = x5 * c / p
    return res


def dx6t(pt, polx12, pi, polx8, pj, polx10, pd, polx17, ps, polx11, polx25,polx30):
    return ((pt * polx12) + (pi * polx8) + (pj * polx10) + (pd * polx17) + ps) * polx11 * polx25 * polx30


def dx7t(x7, g, ig, ng, f, x7x14):
    res = x7 * ((g + ig + ng) / f) * x7x14
    return res


def dx8t(an, ak, p):
    return (an - ak) / p


def dx9t(x9, vn, vk, p, x9x5, x9x6):
    res = x9 * ((vn - vk) / p * x9x5 * x9x6)
    return res


def dx10t(idpn, idpk, p):
    return (idpn - idpk) / p


def dx11t(x11, dpn, dpk):
    res = x11 * (dpn / x11 - dpk / x11)
    return res


def dx12t(bpn, bpk, p):
    return (bpn - bpk) / p


def dx13t(x13, IB, IN, IL, F):
    res = x13 * (IB + IN + IL) / F
    return res


def dx14t(ds, polx15, dv, polx16, dp):
    return (ds * polx15) + (dv * polx16) + dp


def dx15t(x15, jdn, jdk, p):
    res = x15 * (jdn - jdk) / p
    return res


def dx16t(inn, ink, npp):
    return (inn - ink) / npp


def dx17t(x17, ppn, ppk, p):
    res = x17 * (ppn - ppk) / p
    return res


def x18(allIncomeProf, allIncome, polx26):
    return (allIncomeProf / allIncome) * polx26


def dx19t(x19, pbn, pbk, pb):
    res = x19 * (pbn - pbk) / pb
    return res


def dx20t(pmn, pmk, pm):
    return (pmn - pmk) / pm


def dx21t(x21, ipn, ipk):
    res = x21 * (ipn / x21 - ipk / x21)
    return res


def dx22t(opn, opk):
    return opn  - opk


def dx23t(x23, jpn, jpk):
    res = x23 * (jpn / x23 - jpk / x23)
    return res


def dx24t(ispn, ispk, polx26):
    return ispn - (ispk * polx26)


def dx25t(x25, jpn, jpk, p):
    res = x25 * (jpn - jpk) / p
    return res


def dx26t(idpn, polx21, idpk):
    return (idpn * polx21) - idpk


def dx27t(x27, brpn, brpk):
    res = x27 * (brpn / x27 - brpk / x27)
    return res


def dx28t(mrpn, mrpk):
    return mrpn  - mrpk


def dx29t(x29, srpn, srpk):
    res = x29 * (srpn / x29 - srpk / x29)
    return res


def dx30t(rpn, rpk, p):
    return (rpn - rpk) / p


def dx31t(x31, ir, nr, f, x31x30):
    res = x31 * (ir - nr) / f * x31x30
    return res

