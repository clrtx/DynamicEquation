def dx1t(bpn, bpk, polx3, polx19, polx27, polx21, polx22,polx23,polx29):
    res = (bpn * polx3 * polx19 * polx27) - (bpk * polx21 * polx22 * polx23 * polx29)
    return res


def dx2t(x2, mpn, x2x4, x2x20, x2x28, mpk, x2x22, x2x23, x2x29):
    return (((mpn / x2) * x2x4 * x2x20 * x2x28) - ((mpk / x2) * x2x22 * x2x23 * x2x29))


def dx3t(bv, bz, polx3, bc):
    res = ((bv / bz * polx3) - bc / bv)
    return res


def dx4t(x4, mv, mz, x4x20, mc):
    return x4 * ((mv / mz * x4x20) - (mc / mz))


def dx5t(c, p):
    res = c / p
    return res


def dx6t(x6, pt, x6x12, pi, x6x8, pj, x6x10, pd, x6x17, ps):
    return x6 * ((pt * x6x12) + (pi * x6x8) + (pj * x6x10) + (pd * x6x17) + ps)


def dx7t(g, ig, ng, f, polx14):
    res = ((g + ig + ng) / f) * polx14
    return res


def dx8t(x8, an, ak, p):
    return x8 * ((an - ak) / p)


def dx9t(vn, vk, p, polx5, polx6):
    res = ((vn - vk) / p * polx5 * polx6)
    return res


def dx10t(x10, idpn, idpk, p):
    return x10 * ((idpn - idpk) / p)


def dx11t(dpn, dpk):
    res = (dpn - dpk)
    return res


def dx12t(x12, bpn, bpk, p):
    return x12 * ((bpn - bpk) / p)


def dx13t(IB, IN, IL, F):
    res = (IB + IN + IL) / F
    return res


def dx14t(x14, ds, x14x15, dv, x14x16, dp):
    return x14 * ((ds * x14x15) + (dv * x14x16) + dp)


def dx15t(jdn, jdk, p):
    res = (jdn - jdk) / p
    return res


def dx16t(x16, inn, ink, npp):
    return x16 * ((inn - ink) / npp)


def dx17t(ppn, ppk, p):
    res = (ppn - ppk) / p
    return res


def x18(x18, allIncomeProf, allIncome, x18x26):
    return x18 * ((allIncomeProf / allIncome) * x18x26)


def dx19t(pbn, pbk, pb):
    res = (pbn - pbk) / pb
    return res


def dx20t(pmn, pmk, pm):
    return ((pmn - pmk) / pm)


def dx21t(ipn, ipk):
    res = (ipn - ipk)
    return res


def dx22t(x22, opn, opk):
    return x22 * ((opn / x22) - (opk / x22))


def dx23t(jpn, jpk):
    res = (jpn - jpk)
    return res


def dx24t(x24, ispn, ispk, x24x26):
    return x24 * ((ispn / x24) - ((ispk / x24) * x24x26))


def dx25t(jpn, jpk, p):
    res = (jpn - jpk) / p
    return res


def dx26t(x26, idpn, x26x21, idpk):
    return x26 * (((idpn / x26) * x26x21) - (idpk / x26))


def dx27t(brpn, brpk):
    res = (brpn - brpk)
    return res


def dx28t(x28, mrpn, mrpk):
    return x28 * ((mrpn / x28) - (mrpk / x28))


def dx29t(srpn, srpk):
    res = (srpn - srpk)
    return res


def dx30t(x30, rpn, rpk, p):
    return x30 * ((rpn - rpk) / p)


def dx31t(ir, nr, f, polx30):
    res = (ir - nr) / f * polx30
    return res

