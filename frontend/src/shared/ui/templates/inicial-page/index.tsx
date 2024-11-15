import { useState } from 'react'
import BrandButton from '../../atoms/brand-button'
import CinemarkIcon from '../../icons/cinemark'
import MallIcon from '../../icons/mall'
import McDonaldsIcon from '../../icons/mc-donalds'
import NikeIcon from '../../icons/nike'
import RennerIcon from '../../icons/renner'
import Header from '../../molecules/header'
import * as S from './styles'
import Text from '../../atoms/text'

type BrandId = 'renner' | 'mc-donalds' | 'nike' | 'cinemark'

type BrandsType = {
  id: BrandId
  label: string
  icon: JSX.Element
}

const InicialPage = () => {
  const [selectedBrand, setSelectedBrand] = useState<BrandsType | null>(null)

  const brands: BrandsType[] = [
    { id: 'renner', label: 'à Renner', icon: <RennerIcon /> },
    { id: 'mc-donalds', label: 'ao Mc Donalds', icon: <McDonaldsIcon /> },
    { id: 'nike', label: 'à Nike', icon: <NikeIcon /> },
    { id: 'cinemark', label: 'ao Cinemark', icon: <CinemarkIcon /> }
  ]

  return (
    <S.GlobalContainer>
      <Header 
        icon={<MallIcon />} 
        title='Shopping A3' 
      />
      
      <S.Container>
        <S.WrapperBrandButtons>
          {brands.map(brand => (
            <BrandButton 
              isSelected={brand.id === selectedBrand?.id}
              brandIcon={brand.icon}
              onClick={() => { setSelectedBrand(brand) }}  
            />
          ))}
        </S.WrapperBrandButtons>

        <S.WrapperTitleAndSubTitle>
          <Text
            as='h2'
            size={3.2}
            fontFamily='Public Sans'
            weight={700}
            lineHeight={4}
          >
            Bem Vindo ao Shopping A3
          </Text>

          <Text
            size={1.6}
            fontFamily='Public Sans'
            weight={400}
            lineHeight={2.4}
          >
            Aonde vai dessa vez?
          </Text>

          <Text
            size={1.2}
            fontFamily='Public Sans'
            weight={300}
            color='#b0b0b0'
          >
            {selectedBrand && `Então vamos ${selectedBrand.label}? Ótimo!`}
            {!selectedBrand && 'Selecione uma marca acima'}
          </Text>
        </S.WrapperTitleAndSubTitle>

        {selectedBrand && (
          <S.ConfirmButton
            whileHover={{ scale: 1.1 }}
            whileTap={{ scale: 0.9 }}
            onClick={() => {}}
          >
            Confirmar
          </S.ConfirmButton>
        )}
      </S.Container>
    </S.GlobalContainer>
  )
}

export default InicialPage