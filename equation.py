def dx1t(x1, bpn, bpk, x1x3, x1x19, x1x27, x1x21, x1x22, x1x23, x1x29):
    res = x1 * (bpn / x1 * x1x3 * x1x19 * x1x27) - (bpk / x1 * x1x21 * x1x22 * x1x23 * x1x29)
    return res


def dx2t(x2, mpn, x2x4, x2x20, x2x28, mpk, x2x22, x2x23, x2x29):
    return x2 * (((mpn / x2) * x2x4 * x2x20 * x2x28) - ((mpk / x2) * x2x22 * x2x23 * x2x29))


def dx3t(x3, bv, bz, x3x19, bc):
    res = x3 * ((bv / bz * x3x19) - bc / bv)
    return res


def dx4t(x4, mv, mz, x4x20, mc):
    return x4 * ((mv / mz * x4x20) - (mc / mz))


def dx5t(x5, c, p):
    res = x5 * c / p
    return res


def dx6t(x6, pt, x6x12, pi, x6x8, pj, x6x10, pd, x6x17, ps):
    return x6 * ((pt * x6x12) + (pi * x6x8) + (pj * x6x10) + (pd * x6x17) + ps)


def dx7t(x7, g, ig, ng, f, x7x14):
    res = x7 * ((g + ig + ng) / f) * x7x14
    return res


def dx8t(x8, an, ak, p):
    return x8 * ((an - ak) / p)


def dx9t(x9, vn, vk, p, x9x5, x9x6):
    res = x9 * ((vn - vk) / p * x9x5 * x9x6)
    return res


def dx10t(x10, idpn, idpk, p):
    return x10 * ((idpn - idpk) / p)


def dx11t(x11, dpn, dpk):
    res = x11 * (dpn / x11 - dpk / x11)
    return res


def dx12t(x12, bpn, bpk, p):
    return x12 * ((bpn - bpk) / p)


def dx13t(x13, IB, IN, IL, F):
    res = x13 * (IB + IN + IL) / F
    return res


def dx14t(x14, ds, x14x15, dv, x14x16, dp):
    return x14 * ((ds * x14x15) + (dv * x14x16) + dp)


def dx15t(x15, jdn, jdk, p):
    res = x15 * (jdn - jdk) / p
    return res


def dx16t(x16, inn, ink, npp):
    return x16 * ((inn - ink) / npp)


def dx17t(x17, ppn, ppk, p):
    res = x17 * (ppn - ppk) / p
    return res


def x18(x18, allIncomeProf, allIncome, x18x26):
    return x18 * ((allIncomeProf / allIncome) * x18x26)


def dx19t(x19, pbn, pbk, pb):
    res = x19 * (pbn - pbk) / pb
    return res


def dx20t(x20, pmn, pmk, pm):
    return x20 * ((pmn - pmk) / pm)


def dx21t(x21, ipn, ipk):
    res = x21 * (ipn / x21 - ipk / x21)
    return res


def dx22t(x22, opn, opk):
    return x22 * ((opn / x22) - (opk / x22))


def dx23t(x23, jpn, jpk):
    res = x23 * (jpn / x23 - jpk / x23)
    return res


def dx24t(x24, ispn, ispk, x24x26):
    return x24 * ((ispn / x24) - ((ispk / x24) * x24x26))


def dx25t(x25, jpn, jpk, p):
    res = x25 * (jpn - jpk) / p
    return res


def dx26t(x26, idpn, x26x21, idpk):
    return x26 * (((idpn / x26) * x26x21) - (idpk / x26))


def dx27t(x27, brpn, brpk):
    res = x27 * (brpn / x27 - brpk / x27)
    return res


def dx28t(x28, mrpn, mrpk):
    return x28 * ((mrpn / x28) - (mrpk / x28))


def dx29t(x29, srpn, srpk):
    res = x29 * (srpn / x29 - srpk / x29)
    return res


def dx30t(x30, rpn, rpk, p):
    return x30 * ((rpn - rpk) / p)


def dx31t(x31, ir, nr, f, x31x30):
    res = x31 * (ir - nr) / f * x31x30
    return res