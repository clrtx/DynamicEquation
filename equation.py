def dx1t(x1,bpn, bpk, polx3, polx19, polx27, polx21, polx22,polx23,polx29):
    res = (bpn/x1 * polx3 * polx19 * polx27) - (bpk/x1 * polx21 * polx22 * polx23 * polx29)
    return res


def dx2t(x2,mpn, x2x4, polx20, polx28, mpk, polx22, polx23, polx29):
    return (mpn/x2 * x2x4 * polx20 * polx28) - (mpk/x2 * polx22 * polx23 * polx29)


def dx3t(bv, bz, polx3, bc):
    res = ((bv / bz * polx3) - bc / bv)
    return res


def dx4t(mv, mz, polx20, mc):
    return ((mv / mz * polx20) - (mc / mz))


def dx5t(c, p):
    res = c / p
    return res


def dx6t(pt, polx12, pi, polx8, pj, polx10, pd, polx17, ps, polx11, polx25,polx30):
    return ((pt * polx12) + (pi * polx8) + (pj * polx10) + (pd * polx17) + ps) * polx11 * polx25 * polx30


def dx7t(g, ig, ng, f, polx14):
    res = ((g + ig + ng) / f) * polx14
    return res


def dx8t(an, ak, p):
    return (an - ak) / p


def dx9t(vn, vk, p, polx5, polx6):
    res = ((vn - vk) / p * polx5 * polx6)
    return res


def dx10t(idpn, idpk, p):
    return (idpn - idpk) / p


def dx11t(x11,dpn, dpk):
    res = (dpn/x11 - dpk/x11)
    return res


def dx12t(bpn, bpk, p):
    return (bpn - bpk) / p


def dx13t(IB, IN, IL, F):
    res = (IB + IN + IL) / F
    return res


def dx14t(ds, polx15, dv, polx16, dp):
    return (ds * polx15) + (dv * polx16) + dp


def dx15t(jdn, jdk, p):
    res = (jdn - jdk) / p
    return res


def dx16t(inn, ink, npp):
    return (inn - ink) / npp


def dx17t(ppn, ppk, p):
    res = (ppn - ppk) / p
    return res


def x18(allIncomeProf, allIncome, polx26):
    return (allIncomeProf / allIncome) * polx26


def dx19t(pbn, pbk, pb):
    res = (pbn - pbk) / pb
    return res


def dx20t(pmn, pmk, pm):
    return (pmn - pmk) / pm


def dx21t(x21,ipn, ipk):
    res = (ipn/x21 - ipk/x21)
    return res


def dx22t(x22,opn, opk):
    return opn/x22  - opk/x22


def dx23t(x23,jpn, jpk):
    res = (jpn/x23 - jpk/x23)
    return res


def dx24t(x24,ispn, ispk, polx26):
    return ispn/x24 - (ispk/x24 * polx26)


def dx25t(jpn, jpk, p):
    res = (jpn - jpk) / p
    return res


def dx26t(x26,idpn, polx21, idpk):
    return (idpn/x26 * polx21) - idpk/x26


def dx27t(x27,brpn, brpk):
    res = (brpn/x27 - brpk/x27)
    return res


def dx28t(x28,mrpn, mrpk):
    return mrpn/x28  - mrpk/x28


def dx29t(x29,srpn, srpk):
    res = (srpn/x29 - srpk/x29)
    return res


def dx30t(rpn, rpk, p):
    return (rpn - rpk) / p


def dx31t(ir, nr, f, polx30):
    res = (ir - nr) / f * polx30
    return res

